
import requests
import json

def emotion_detector(text_to_analyze):  
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        myobj = { "raw_document": { "text": text_to_analyze } }
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        response = requests.post(url, json = myobj, headers=header) 
        formatted_response = json.loads(response.text) 
        
        pprint.pprint(formatted_response)

        if not response.text or not response.text.strip() or not text_to_analyse or not text_to_analyse.strip():
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None 
            } 


        if response.status_code == 200:
            emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
            
            # Extract individual emotions
            anger = emotion_predictions['anger']
            disgust = emotion_predictions['disgust']
            fear = emotion_predictions['fear']
            joy = emotion_predictions['joy']
            sadness = emotion_predictions['sadness']
            
            # Find the dominant emotion (the one with the highest score)
            emotion_list = [
                {'anger': anger},
                {'disgust': disgust},
                {'fear': fear},
                {'joy': joy},
                {'sadness': sadness}
            ]
            
            dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
            
            # Return the formatted dictionary required for Task 3
            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        elif response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }        

    except requests.exceptions.RequestException:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except (KeyError, IndexError, json.JSONDecodeError):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }            