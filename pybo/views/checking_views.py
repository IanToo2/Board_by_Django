import requests
from django.shortcuts import render

def answer_filter(request):
    return render(request, 'pybo/answer_form.html')

def process_api_request(request):
    if request.method == 'POST':
        # API 요청 보내기
        url = "https://api.matgim.ai/54edkvw2hn/api-keyword-slang"
        headers = {
            "content-type": "application/json",
            "x-auth-token": "d76aba63-b75e-4d35-9141-62076480c283"
        }
        data = {
            "document": "비속어를 추출할 대상 텍스트가 들어갈 자리입니다."
        }
        response = requests.post(url, headers=headers, json=data)

        # 응답 처리 및 템플릿에 결과 전달
        if response.status_code == 200:
            result = response.json()
            api_data = result.get("result", {}).get("data", [])

            return render(request, 'pybo/answer_form.html', {'api_data': api_data})
        else:
            error_message = f"Error: {response.status_code}"
            return render(request, 'pybo/answer_form.html', {'error_message': error_message})

    return render(request, 'pybo/answer_form.html')
