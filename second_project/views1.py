from django.http import HttpResponse
from django.shortcuts import render
import string

def index1(request):
    
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get("text")
    print(djtext)
    remove_punc = request.POST.get("removepunc", 'off')
    uppercase = request.POST.get("uppercase", 'off')
    newlineremover = request.POST.get("newlineremover", 'off')
    extraspaceremover = request.POST.get('extraspacerem', 'off')
    print(extraspaceremover)
    character_counter = request.POST.get('countchar', 'off')
    # print(character_counter)
    # punctutions = list(string.punctuation)
    punctutions = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    # print(punctutions)
    analyzed = ""
    purpose = ""

    if remove_punc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctutions:
                print(char)
                analyzed = analyzed + char 
        djtext = analyzed
        purpose = purpose + 'Removed Punctuations, '
        # params = {'purpose': 'Removed Punctuations', 'Analyzed_text':analyzed}
        # return render(request, 'analyze.html', params)

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose = purpose + 'Changed to Upper Case, '
        # params = {'purpose' : 'Changed to upper case', 'Analyzed_text' : analyzed}
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + 'Removed New Line, '
        # params = {'purpose' : 'New line removed', 'Analyzed_text' : analyzed }
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        djtext_list = djtext.split(" ")
        # print(djtext_list)
        # for i in range(0, len(djtext_list)):
        #     if djtext_list[i] == " ":
        #         pass
        #     else:
        #         if i == 0:
        #             analyzed = analyzed + str(djtext_list[i])
        #         else:
        #             analyzed = analyzed + " " + djtext_list[i]
        #             print(analyzed)

        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " ") :
                analyzed = analyzed + djtext[index]
        djtext = analyzed
        purpose = purpose + 'Removed Extra Space, '
        # params = {'purpose' : 'Extra Space Remover', 'Analyzed_text' : analyzed}
        # return render(request, 'analyze.html', params)

    if character_counter == "on":
        analyzed = ""
        counter = 0
        for char in djtext:
            counter = counter + 1
        analyzed = 'Your updated text is : ' + djtext +  ' , with total characters : ' +  str(counter)
        djtext = analyzed
        purpose = purpose + 'Counted Total Characters, '
        # params = {'purpose' : 'Counted the number of characters', 'Analyzed_text' : 'The number of characters in djtext are: ' + str(counter)}
        # return render(request, 'analyze.html', params)
    
    if (remove_punc!="on" and uppercase!="on" and newlineremover!="on" and extraspaceremover=="on" and character_counter=="on"):
        return HttpResponse("error")
    
    params = {'purpose' : purpose, 'Analyzed_text' : analyzed}
    return render(request, 'analyze.html', params)
    
