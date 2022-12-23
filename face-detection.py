import boto3
import json


def detect_face(photo, bucket):
    client=boto3.client('rekognition')
    response = client.detect_faces(Image={'S3Object':
    {'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
    print('Detected faces for ' + photo)
    return response

def main():
    s3 = boto3.resource('s3')
    bucket_name = 'r0835034-cloud-fundamentals' 
    given_bucket = s3.Bucket(bucket_name)

    responses = list()

    for image in given_bucket.objects.all():
        face = detect_face(image.key, bucket_name)
        responses.append(face)

    jsons_responses = json.dumps(responses)
    output_file = "detected_faces.json"

    with open(output_file, "w") as file:
        file.write(jsons_responses)

if __name__ == "__main__":
    main()