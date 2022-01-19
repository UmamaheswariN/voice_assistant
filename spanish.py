import requests

from aide_MultiLang import there_exists, translator, convert_language, talk, talk_command, stopspeacking


class SpanishService(object):
    def __init__(self):
        pass

    def convert_language(self,command, language_code):
        # invoking Translator
        if 'spanish' in language_code or 'french' in language_code:
            if 'spanish' in language_code:
                translate_text = translator.translate(command, dest='es')
                return translate_text.text

    def get_spanish_data(self, choosenLangCode):
        if there_exists(["solicitud de banco", "asunto", "asanthu", "assunto",
                         "Crear Ticket"]):
            audio_string = "Happy to assist you! Can you tell your name"
            print(audio_string)
            if 'spanish' in choosenLangCode or 'french' in choosenLangCode or 'english' in choosenLangCode:
                destini_lang0 = convert_language(audio_string, choosenLangCode)
                talk(destini_lang0)
                print(destini_lang0)
                requesterName = talk_command()
                print(requesterName)
                if 'None' in requesterName:
                    audio_string1 = "Pardon! Can you tell your name again"
                    print(audio_string1)
                    destini_lang110 = convert_language(audio_string1, choosenLangCode)
                    print(destini_lang110)
                    talk(destini_lang110)
                    requesterName = talk_command()
                    print(requesterName)
                else:
                    audio_string2 = "Can you tell your stationName"
                    print(audio_string2)
                    destini_lang2 = convert_language(audio_string2, choosenLangCode)
                    print(destini_lang2)
                    talk(destini_lang2)
                    stationName = talk_command()
                    print(stationName)
                    if 'None' in stationName:
                        audio_string3 = "Pardon! Can you tell your stationName again"
                        print(audio_string3)
                        destini_lang3 = convert_language(audio_string3, choosenLangCode)
                        print(destini_lang3)
                        talk(destini_lang3)
                        stationName = talk_command()
                        print(stationName)
                    else:
                        audio_string4 = "Can you describe issue"
                        print(audio_string4)
                        destini_lang4 = convert_language(audio_string4, choosenLangCode)
                        print(destini_lang4)
                        talk(destini_lang4)
                        reqIssueDescription = talk_command()
                        print(reqIssueDescription)
                        if 'None' in reqIssueDescription:
                            audio_string5 = "Pardon! Can you describe the issue once again"
                            print(audio_string5)
                            destini_lang5 = convert_language(audio_string5, choosenLangCode)
                            print(destini_lang5)
                            talk(destini_lang5)
                            reqIssueDescription = talk_command()
                            print(reqIssueDescription)
                        else:
                            if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                                audio_string6 = "Pardon! The request not created due to invalid values.Please repeat"
                                print(audio_string6)
                                destini_lang6 = convert_language(audio_string6, choosenLangCode)
                                print(destini_lang6)
                                talk(destini_lang6)
                            else:
                                audio_string7 = "I am confirming the details as you given"
                                print(audio_string7)
                                destini_lang7 = convert_language(audio_string7, choosenLangCode)
                                talk(destini_lang7)
                                audio_string8 = "your name"
                                print(audio_string8)
                                destini_lang8 = convert_language(audio_string8, choosenLangCode)
                                print(destini_lang8)
                                talk(destini_lang8)
                                talk(requesterName)
                                audio_string9 = "your station name"
                                print(audio_string9)
                                destini_lang9 = convert_language(audio_string9, choosenLangCode)
                                print(destini_lang9)
                                talk(destini_lang9)
                                talk(stationName)
                                audio_string10 = "your issue description"
                                print(audio_string10)
                                destini_lang10 = convert_language(audio_string10, choosenLangCode)
                                print(destini_lang10)
                                talk(destini_lang10)
                                talk(reqIssueDescription)
                                audio_string11 = "All these details are okay? Shall i proceed to create? please confirm yes or no"
                                print(audio_string11)
                                destini_lang11 = convert_language(audio_string11, choosenLangCode)
                                print(destini_lang11)
                                talk(destini_lang11)
                                confirmCreateRequest = talk_command()
                                if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest:
                                    print('BenchRequest Service..')
                                    benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                                    benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                                 "stationId": 0, "stationName": stationName, "siteId": 1004, "statusId": 3,
                                                 "categoryId": 1, "subcategoryId": 1, "assigneeId": 7668, "priority": 0,
                                                 "repairAction1Id": 0, "repairAction2Id": 0, "repairAction3Id": 0,
                                                 "diagnosisId": 0,
                                                 "sBUId": 1, "systemId": 0, "description": reqIssueDescription,
                                                 "comments": "test", "userId": 0, "requesterEmail": '',
                                                 "supervisorId": 7687, "email": '',
                                                 "supervisorName": "CiscoSupervisor", "userfor": "requester",
                                                 "status": "Assigned",
                                                 "docs": ""}
                                    print(benchData)

                                    headers = {'Content-type': 'application/json'}
                                    print('BenchRequest Service call in progress..')
                                    # responeData = requests.put(benchReqUrl, json={'json_payload': data}, headers=headers)
                                    responeData = requests.put(benchReqUrl, headers=headers, data=json.dumps(benchData))
                                    print(responeData.json())
                                    print(responeData)
                                    if '<Response [200]>' in responeData:
                                        audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                        print(audio_string12)
                                        destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                        talk(destini_lang12)
                                        print(destini_lang12)
                                        stopspeacking()
                                    else:
                                        audio_string13 = 'Thanks for using R1.0'
                                        print(audio_string13)
                                        destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                        talk(destini_lang13)
                                        print(destini_lang13)
                                        stopspeacking()
                                elif 'no' in confirmCreateRequest:
                                    audio_string14 = 'This issue will not create without your confirmation.'
                                    print(audio_string14)
                                    destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                    print(audio_string14)
                                    talk(destini_lang14)
                                    stopspeacking()
            elif 'tamil' in choosenLangCode or 'hindi' in choosenLangCode:
                destini_lang0 = convert_language(audio_string, choosenLangCode)
                #talk(destini_lang0)
                print(destini_lang0)
                requesterName = talk_command()
                print(requesterName)
                if 'None' in requesterName:
                    audio_string1 = "Pardon! Can you tell your name again"
                    print(audio_string1)
                    destini_lang110 = convert_language(audio_string1, choosenLangCode)
                    print(destini_lang110)
                    #talk(destini_lang110)
                    requesterName = talk_command()
                    print(requesterName)
                else:
                    audio_string2 = "Can you tell your stationName"
                    print(audio_string2)
                    destini_lang2 = convert_language(audio_string2, choosenLangCode)
                    print(destini_lang2)
                    #talk(destini_lang2)
                    stationName = talk_command()
                    print(stationName)
                    if 'None' in stationName:
                        audio_string3 = "Pardon! Can you tell your stationName again"
                        print(audio_string3)
                        destini_lang3 = convert_language(audio_string3, choosenLangCode)
                        print(destini_lang3)
                        #talk(destini_lang3)
                        stationName = talk_command()
                        print(stationName)
                    else:
                        audio_string4 = "Can you describe issue"
                        print(audio_string4)
                        destini_lang4 = convert_language(audio_string4, choosenLangCode)
                        print(destini_lang4)
                        #talk(destini_lang4)
                        reqIssueDescription = talk_command()
                        print(reqIssueDescription)
                        if 'None' in reqIssueDescription:
                            audio_string5 = "Pardon! Can you describe the issue once again"
                            print(audio_string5)
                            destini_lang5 = convert_language(audio_string5, choosenLangCode)
                            print(destini_lang5)
                           #talk(destini_lang5)
                            reqIssueDescription = talk_command()
                            print(reqIssueDescription)
                        else:
                            if 'None' in requesterName or 'None' in stationName or 'None' in reqIssueDescription:
                                audio_string6 = "Pardon! The request not created due to invalid values.Please repeat"
                                print(audio_string6)
                                destini_lang6 = convert_language(audio_string6, choosenLangCode)
                                print(destini_lang6)
                                #talk(destini_lang6)
                            else:
                                audio_string7 = "I am confirming the details as you given"
                                print(audio_string7)
                                destini_lang7 = convert_language(audio_string7, choosenLangCode)
                                #talk(destini_lang7)
                                audio_string8 = "your name"
                                print(audio_string8)
                                destini_lang8 = convert_language(audio_string8, choosenLangCode)
                                print(destini_lang8)
                                #talk(destini_lang8)
                                talk(requesterName)
                                audio_string9 = "your station name"
                                print(audio_string9)
                                destini_lang9 = convert_language(audio_string9, choosenLangCode)
                                print(destini_lang9)
                                #talk(destini_lang9)
                                talk(stationName)
                                audio_string10 = "your issue description"
                                print(audio_string10)
                                destini_lang10 = convert_language(audio_string10, choosenLangCode)
                                print(destini_lang10)
                                #talk(destini_lang10)
                                talk(reqIssueDescription)
                                audio_string11 = "All these details are okay? Shall i proceed to create? please confirm yes or no"
                                print(audio_string11)
                                destini_lang11 = convert_language(audio_string11, choosenLangCode)
                                print(destini_lang11)
                                #talk(destini_lang11)
                                confirmCreateRequest = talk_command()
                                if 'yes' in confirmCreateRequest or 's' in confirmCreateRequest or 'z' in confirmCreateRequest:
                                    print('BenchRequest Service..')
                                    benchReqUrl = "http://localhost:4301/api/BenchRequests/BenchRequestSave"
                                    benchData = {"id": 0, "requestorId": 0, "requesterName": requesterName,
                                                 "stationId": 0, "stationName": stationName, "siteId": 1004,
                                                 "statusId": 3,
                                                 "categoryId": 1, "subcategoryId": 1, "assigneeId": 7668, "priority": 0,
                                                 "repairAction1Id": 0, "repairAction2Id": 0, "repairAction3Id": 0,
                                                 "diagnosisId": 0,
                                                 "sBUId": 1, "systemId": 0, "description": reqIssueDescription,
                                                 "comments": "test", "userId": 0, "requesterEmail": '',
                                                 "supervisorId": 7687, "email": '',
                                                 "supervisorName": "CiscoSupervisor", "userfor": "requester",
                                                 "status": "Assigned",
                                                 "docs": ""}
                                    print(benchData)

                                    headers = {'Content-type': 'application/json'}
                                    print('BenchRequest Service call in progress..')
                                    # responeData = requests.put(benchReqUrl, json={'json_payload': data}, headers=headers)
                                    responeData = requests.put(benchReqUrl, headers=headers, data=json.dumps(benchData))
                                    print(responeData.json())
                                    print(responeData)
                                    if '<Response [200]>' in responeData:
                                        audio_string12 = 'Successfully created your ticket in Bench request. Thanks for using R1.0'
                                        print(audio_string12)
                                        destini_lang12 = convert_language(audio_string12, choosenLangCode)
                                       # talk(destini_lang12)
                                        print(destini_lang12)
                                        stopspeacking()
                                    else:
                                        audio_string13 = 'Thanks for using R1.0'
                                        print(audio_string13)
                                        destini_lang13 = convert_language(audio_string13, choosenLangCode)
                                        #talk(destini_lang13)
                                        print(destini_lang13)
                                        stopspeacking()
                                elif 'no' in confirmCreateRequest:
                                    audio_string14 = 'This issue will not create without your confirmation.'
                                    print(audio_string14)
                                    destini_lang14 = convert_language(audio_string14, choosenLangCode)
                                    print(audio_string14)
                                   #talk(destini_lang14)
                                    stopspeacking()
        return "true"
