from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from django.core.files.base import ContentFile
import codecs

def project_detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        if not project.document:
            return JsonResponse({'error': 'Original document not found'}, status=404)

        # Читаем содержимое файлов
        with open(project.document.path, 'r', errors='ignore') as original_doc_file:
            original_doc_content = original_doc_file.read()

        if project.tr_document:
            with open(project.tr_document.path, 'r', errors='ignore') as translated_doc_file:
                translated_doc_content = translated_doc_file.read()
        else:
            translated_doc_content = ''

        context = {
            'project': project,
            'original_doc_content': original_doc_content,
            'translated_doc_content': translated_doc_content,
            'activity':project.activities.all()[0]
        }
        return render(request, 'editor_file.html', context)

    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)






def save_translated_document(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        translated_content = request.POST.get('translated_content', '')

        # Сохраняем только переведенный документ
        if translated_content:
            project.tr_document.save(f"translated_{project.document.name}", ContentFile(translated_content), save=True)
            return JsonResponse({'message': 'Translated document saved successfully'})
        else:
            return JsonResponse({'error': 'Translated content is empty'}, status=400)

    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
