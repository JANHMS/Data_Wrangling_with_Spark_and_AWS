import boto3

def create_s3_bucket():
    '''Create the bucket root and the folders in AWS S3
    Parameters:
    -----------
    s3: object
    bucket_root: string - name of the bucket
    keys: list - folder_names(string) within the bucket
    
    Returns:
    --------
    Nothing
    
    Notes
    -----
    This method does not return anything, but it creates a bucket within our AWS S3. 
    '''
    try:
        bucket_root='janneman-udacity-sparkify-data-lake'

        client = boto3.client('s3', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],               aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
)
        client.create_bucket(ACL='private',Bucket=bucket_root,
                            CreateBucketConfiguration
                            {'LocationConstraint':'us-west-2'})

    except Exception as e:
        raise e

    # bucket = s3.Bucket(bucket_root)
    folders_name = ['songs','songplays','time','artists','users']


    # Create folders for the tables
    for f in folders_name:
        fold_name = f'{f}/'
        try: 
            client.put_object(Bucket=bucket_root ,Key=fold_name)
        except Exception as e:
            raise e
    print('Folders created')
            
if __name__=='__main__':
    
    create_s3_bucket()