from celery import shared_task
import boto3
import sched, time
import requests
s = sched.scheduler(time.time, time.sleep)


@shared_task
def create_task(id, name):
    session = boto3.Session(
            aws_access_key_id='AKIAZVZNJBXI35X2S4MP',
            aws_secret_access_key='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'
        )
    s3 = session.resource('s3')
    result = s3.Bucket('vh-s3').download_file('{}/{}'.format(str(id), name), name)
        
    counter = 0
    s.enter(1, 2, do_delay, (s,id, counter))
    s.run()
    r = requests.patch('http://127.0.0.1:8000/api/video/update/{}/'.format(id), json={"result": "success"})
    with open('result.txt', 'w') as f:
        f.write(str(video_duration(name)))
        
    result = s3.Bucket('vh-s3').put_object(Body=open('result.txt', 'rb'), Key='{}/{}'.format(str(id), 'result.txt'))
    return True

def do_delay(sc, id, counter):
    
    r = requests.patch('http://127.0.0.1:8000/api/video/update/{}/'.format(id), json={"result": "in_progress", "progress": counter})
    if counter == 10:
        return
    counter = counter+1
    sc.enter(1, 100, do_delay, (sc, id, counter))



import cv2
def video_duration(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration_sec = int(num_frames / fps)
    return duration_sec