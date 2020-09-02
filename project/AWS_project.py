import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import filedialog
from cryptography.fernet import Fernet
from PIL import Image
import os
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import boto3

#This is the main class
class SampleApp(tk.Tk):
    
    

    def __init__(self, *args, **kwargs):
        
            
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Encryption Model Simulation")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        global container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.fun(StartPage)
        
        self.show_frame("StartPage")

#Function to execute the class and add it to the stack for displaying
    def fun(self,x):
        F=x
        page_name = F.__name__
        frame = F(parent=container, controller=self)
        self.frames[page_name] = frame
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

#Function to display selected page
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#login Page
class StartPage(tk.Frame):
            
    def __init__(self, parent, controller):
        def close():
            app.destroy()
        def hello ():
            global access_key_id
            global access_key_password
            global client
            access_key_id=text1.get("1.0","end-1c")
            access_key_password=text2.get("1.0","end-1c")
            text1.delete("1.0","end")
            text2.delete("1.0","end")
            text1.insert(tk.INSERT,"AWS IAM user_name")
            text2.insert(tk.INSERT,"AWS Password")
            try:
                client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password)
                response = client.list_buckets()
                controller.fun(Decide)
                controller.fun(pageb)
                controller.show_frame("Decide")
            except Exception as e:
                label1=tk.Label(self, text= e, fg='black', font=('helvetica', 12))
                canvas1.create_window(300, 400, window=label1)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        button = tk.Button(self, text="Close", command=close)
        canvas1.create_window(575, 10, window=button)
        heading=tk.Label(self,text="Login into AWS IAM using credentials", font=("arial", 18, "bold"), fg="steelblue")
        canvas1.create_window(300, 250, window=heading)
        label1 = tk.Label(self, text= 'Username', fg='black', font=('helvetica', 18, 'bold'))
        canvas1.create_window(250, 300, window=label1)
        text1=tk.Text(self,height=1,width=20)
        canvas1.create_window(400, 300, window=text1)
        text1.insert(tk.INSERT,"AWS IAM user_name")
        label2 = tk.Label(self, text= 'Password', fg='black', font=('helvetica', 18, 'bold'))
        canvas1.create_window(250, 325, window=label2)
        text2=tk.Text(self,height=1,width=20)
        text2.insert(tk.INSERT,"AWS Password")
        canvas1.create_window(400, 325, window=text2)
        button1 = tk.Button(self, text='Login',command=hello,font=('helvetica', 18, 'bold'))
        #button1 = tk.Button(self, text="Login",command=lambda: controller.show_frame("PageOne"))
        canvas1.create_window(320, 350, window=button1)

#page to decide if user want to download or upload
class Decide(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        def up():
            controller.fun(PageOne)
            controller.show_frame("PageOne")
        def down():
            controller.fun(Download)
            controller.show_frame("Download")
        button1 = tk.Button(self, text="upload_files to S3", command=up)
        canvas1.create_window(250, 150, window=button1)
        button2 = tk.Button(self, text="Download files from S3", command=down)
        canvas1.create_window(250, 190, window=button2)
        button = tk.Button(self, text="Logout", command=lambda:controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        

#home page for download
class Download(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        def modela():
            controller.fun(DownloadA)
            controller.show_frame("DownloadA")
        def modelc():
            controller.fun(DownloadC)
            controller.show_frame("DownloadC")
        def modelb():
            controller.show_frame("pageb")
        def modela_info():
            im = Image.open(r"modela.PNG")
            im.show()
        def modelb_info():
            im = Image.open(r"modelb.PNG")
            im.show()
        def modelc_info():
            im = Image.open(r"modelc.PNG")
            im.show()
        button = tk.Button(self, text="Logout", command=lambda:controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=lambda:controller.show_frame("Decide"))
        canvas1.create_window(575, 30, window=buttona)
        label1=tk.Label(self, text="Select from below Models of Encryption to upload the file", font=('helvetica', 18, 'bold'))
        canvas1.create_window(250,40, window=label1)
        button = tk.Button(self, text="\n\n\n   MODEL A   \n\n\n", command=modela)
        canvas1.create_window(130, 180, window=button)
        button = tk.Button(self, text="\n\n\n   MODEL B   \n\n\n", command=modelb)
        canvas1.create_window(230, 180, window=button)
        button = tk.Button(self, text="\n\n\n   MODEL C   \n\n\n", command=modelc)
        canvas1.create_window(330, 180, window=button)
        button4 = tk.Button(self, text="more info..", command=modela_info)
        canvas1.create_window(130, 250, window=button4)
        button5 = tk.Button(self, text="more info..", command=modelb_info)
        canvas1.create_window(230, 250, window=button5)
        button6 = tk.Button(self, text="more info..", command=modelc_info)
        canvas1.create_window(330, 250, window=button6)

#Model A download page
class DownloadA(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        canvas2 = tk.Canvas(self, width = 300, height = 300)
        canvas2.pack()
        canvas1.create_window(400, 400, window=canvas2)
        canvas3 = tk.Canvas(self, width = 50, height = 50)
        canvas3.pack()
        canvas1.create_window(320, 100, window=canvas3)
        def logout():
            canvas3.delete("all")
            controller.show_frame("StartPage")
        def home():
            canvas3.delete("all")
            controller.show_frame("Decide")
        button = tk.Button(self, text="Logout", command=logout)
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=home)
        canvas1.create_window(575, 30, window=buttona)
        def path():
            path=filedialog.askopenfilename(initialdir = "/",title = "Select key file")
            text1.delete("1.0","end")
            text1.insert(tk.INSERT,path)
        def download():
            canvas2.delete("all")
            bucket=variable.get()
            Object_name=text2.get("1.0","end-1c")
            file_name=text3.get("1.0","end-1c")+'/'+Object_name
            print(file_name)
            try:
                client.download_file(bucket,Object_name,file_name)
                key = open(text1.get("1.0","end-1c"), "rb").read()
                f = Fernet(key)
                with open(file_name, "rb") as file:
                    encrypted_data = file.read()

                # decrypt data
                decrypted_data = f.decrypt(encrypted_data)
                # write the original file
                with open(file_name, "wb") as file:
                    file.write(decrypted_data)
                label6=tk.Label(self, text= 'Download success!!', fg='black', font=('helvetica', 14))
                canvas2.create_window(0, 100, window=label6)
            except Exception as e:
                canvas2.delete("all")
                self.update()
                label6=tk.Label(self, text= e, fg='black', font=('helvetica', 14))
                canvas2.create_window(0, 100, window=label6)

        label1 = tk.Label(self, text= 'Select Bucket:', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 100, window=label1)
        
        collection=[]
        client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password)
        response = client.list_buckets()
        if response['Buckets']!=[]:
            for bucket in response['Buckets']:
                collection.append(bucket["Name"])
            #app = tk.Tk()
            variable = tk.StringVar()
            variable.set(collection[0])
            opt = tk.OptionMenu(app, variable, *collection)
            canvas3.create_window(30,30, window=opt)
        else:
            label5=tk.Label(self, text= 'No existing Buckets', fg='black', font=('helvetica', 18))
            canvas1.create_window(320, 100, window=label5)
        label1 = tk.Label(self, text= 'Give file name', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 130, window=label1)
        text2=tk.Text(self,height=1,width=20)
        canvas1.create_window(320, 130, window=text2)
        text2.insert(tk.INSERT,"File_name")
        label2 = tk.Label(self, text= 'Provide Key path for Decryption:', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 160, window=label2)
        text1=tk.Text(self,height=1,width=20)
        canvas1.create_window(320, 160, window=text1)
        text1.insert(tk.INSERT,"Key-path")
        button1 = tk.Button(self, text='...',command=path)
        canvas1.create_window(400, 160, window=button1)
        label3 = tk.Label(self, text= 'Provide path to save file:', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 190, window=label3)
        text3=tk.Text(self,height=1,width=20)
        canvas1.create_window(320, 190, window=text3)
        text3.insert(tk.INSERT,"Destination path")
        button2 = tk.Button(self, text='Download',command=download)
        canvas1.create_window(300, 250, window=button2)
        
#model c download page
class DownloadC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        canvas2 = tk.Canvas(self, width = 300, height = 300)
        canvas2.pack()
        canvas1.create_window(400, 400, window=canvas2)
        canvas3 = tk.Canvas(self, width = 50, height = 50)
        canvas3.pack()
        canvas1.create_window(320, 100, window=canvas3)
        def logout():
            canvas3.delete("all")
            controller.show_frame("StartPage")
        def home():
            canvas3.delete("all")
            controller.show_frame("Decide")
        button = tk.Button(self, text="Logout", command=logout)
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=home)
        canvas1.create_window(575, 30, window=buttona)
        def download():
            canvas2.delete("all")
            bucket=variable.get()
            Object_name=text2.get("1.0","end-1c")
            file_name=text3.get("1.0","end-1c")+'/'+Object_name
            print(file_name)
            try:
                client.download_file(bucket,Object_name,file_name)
                label6=tk.Label(self, text= 'Download success!!', fg='black', font=('helvetica', 14))
                canvas2.create_window(0, 100, window=label6)
            except Exception as e:
                canvas2.delete("all")
                self.update()
                label6=tk.Label(self, text= e, fg='black', font=('helvetica', 14))
                canvas2.create_window(0, 100, window=label6)
        label1 = tk.Label(self, text= 'Select Bucket:', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 100, window=label1)
        collection=[]
        client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password)
        response = client.list_buckets()
        if response['Buckets']!=[]:
            for bucket in response['Buckets']:
                collection.append(bucket["Name"])
            #app = tk.Tk()
            variable = tk.StringVar()
            variable.set(collection[0])
            opt = tk.OptionMenu(app, variable, *collection)
            canvas3.create_window(30,30, window=opt)
        else:
            label5=tk.Label(self, text= 'No existing Buckets', fg='black', font=('helvetica', 18))
            canvas1.create_window(320, 100, window=label5)
        label1 = tk.Label(self, text= 'Give file name', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 130, window=label1)
        text2=tk.Text(self,height=1,width=20)
        canvas1.create_window(320, 130, window=text2)
        text2.insert(tk.INSERT,"File_name")
        label3 = tk.Label(self, text= 'Provide path to save file:', fg='black', font=('helvetica', 14))
        canvas1.create_window(120, 190, window=label3)
        text3=tk.Text(self,height=1,width=20)
        canvas1.create_window(320, 190, window=text3)
        text3.insert(tk.INSERT,"Destination path")
        button2 = tk.Button(self, text='Download',command=download)
        canvas1.create_window(300, 250, window=button2)

#Upload otipn page 1
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        canvas2 = tk.Canvas(self, width = 300, height = 300)
        canvas2.pack()
        canvas1.create_window(400, 400, window=canvas2)
        def create_bucket():
            global bucket_name
            bucket_name=text1.get("1.0","end-1c")
            region=text2.get("1.0","end-1c")
            try:
                s3_client = boto3.client('s3', region_name=region,aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
                canvas2.delete("all")
                controller.fun(PageTwo)
                controller.show_frame("PageTwo")
            except Exception as e:
                label=tk.Label(self, text=e,fg='black', font=('helvetica', 12))
                canvas2.create_window(40,150, window=label)
        def bucket_select():
            global bucket_name
            bucket_name=variable.get()
            canvas2.delete("all")
            controller.fun(PageTwo)
            controller.show_frame("PageTwo")
        def exist():
            global variable
            canvas2.delete("all")
            canvas2.create_window(0, 0, window=label1)
            collection=[]
            response = client.list_buckets()
            if response['Buckets']!=[]:
                for bucket in response['Buckets']:
                    collection.append(bucket["Name"])
                #app = tk.Tk()
                variable = tk.StringVar()
                variable.set(collection[0])
                opt = tk.OptionMenu(app, variable, *collection)
                #opt.pack()
                #opt.config(width=90, font=('Helvetica', 12))
                
                canvas2.create_window(0, 60, window=opt)
                button1 = tk.Button(self, text='Select',command=bucket_select)
                canvas2.create_window(0, 100, window=button1)
            else:
                label5=tk.Label(self, text= 'No existing Buckets please create a new one to upload file', fg='black', font=('helvetica', 18, 'bold'))
                canvas2.create_window(50,100, window=label5)
        def new():
            canvas2.delete("all")
            canvas2.create_window(0, 0, window=label2)
            canvas2.create_window(0, 45, window=label3)
            canvas2.create_window(150, 45, window=text1)
            canvas2.create_window(0, 75, window=label4)
            canvas2.create_window(150, 75, window=text2)
            button1 = tk.Button(self, text='Create',command=create_bucket)
            #button1 = tk.Button(self, text="Login",command=lambda: controller.show_frame("PageOne"))
            canvas2.create_window(50, 120, window=button1)
        def logout():
            canvas2.delete("all")
            controller.show_frame("StartPage")
        def home():
            canvas2.delete("all")
            controller.show_frame("Decide")
        button = tk.Button(self, text="Logout", command=logout)
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=home)
        canvas1.create_window(575, 30, window=buttona)
        label1 = tk.Label(self, text= 'Select from below list of existing buckets', fg='black', font=('helvetica', 18, 'bold'))
        label2 = tk.Label(self, text= 'Provide below details for creating new S3 bucket', fg='black', font=('helvetica', 18, 'bold'))
        button1 = tk.Button(self, text="Use existing S3 bucket to upload files", command=exist)
        canvas1.create_window(250, 150, window=button1)
        button2 = tk.Button(self, text="Create new S3 bucket to upload files", command=new)
        canvas1.create_window(250, 190, window=button2)
        label3 = tk.Label(self, text= 'Bucket_name', fg='black', font=('helvetica', 18, 'bold'))
        text1=tk.Text(self,height=1,width=20)
        text1.insert(tk.INSERT,"bucket name")
        label4 = tk.Label(self, text= 'Region*', fg='black', font=('helvetica', 18, 'bold'))
        text2=tk.Text(self,height=1,width=20)
        text2.insert(tk.INSERT,"Cannot be None")

#upload option page 2
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        canvas2 = tk.Canvas(self, width = 300, height = 300)
        canvas2.pack()
        canvas1.create_window(400, 400, window=canvas2)
        def file():
            canvas2.delete("all")
            global filename
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select file to upload")
            disp="file selected to upload:\n"+filename
            label2=tk.Label(self, text= disp, fg='black', font=('helvetica', 18, 'bold'))
            canvas2.create_window(0, 0, window=label2)
            button1=tk.Button(self,text="Confirm selection", command=three)
            canvas2.create_window(0, 50, window=button1)
        def three():
            controller.fun(PageThree)
            controller.show_frame("PageThree")
        global bucket_name
        display='Bucket selected to upload the files:\n'+bucket_name
        label1 = tk.Label(self, text= display, fg='black', font=('helvetica', 18, 'bold'))
        canvas1.create_window(250, 100, window=label1)
        button = tk.Button(self, text="Logout", command=lambda: controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=lambda:controller.show_frame("Decide"))
        canvas1.create_window(575, 30, window=buttona)
        button = tk.Button(self, text="Change bucket selection", command=lambda: controller.show_frame("PageOne"))
        canvas1.create_window(250, 150, window=button)
        button = tk.Button(self, text="select file to upload", command=file)
        canvas1.create_window(250, 200, window=button)

#common page model b
class pageb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        button = tk.Button(self, text="Logout", command=lambda:controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=lambda:controller.show_frame("Decide"))
        canvas1.create_window(575, 30, window=buttona)
        matter="Model B requires AWS CloudHSM which is a paid service, because of cost issue this \nis not being implemented in the project. CloudHSM requires that a VPC, a private subnet, \nand a Cluster are created. A cluster is a collection of individual HSMs.\nAWS CloudHSM synchronizes the HSMs in each cluster so that they function as one logical unit. \nWe can use AWS CloudHSM API to create a cluster by sending a CreateCluster request. When you \ncreate a cluster, a security group with the name “cloudhsm-cluster-clusterID-sg” is \nautomatically created which contains a preconfigured TCP rule that allows inbound and \noutbound communication within the cluster security group over ports 2223-2225. This rule \nallows HSMs in the cluster to communicate with each other. The next step is to launch an \nEC2 instance and connect it to AWS CloudHSM cluster. We are now ready to create a HSM \nwhich can be accomplished by sending a CreateHSM request through the CloudHSM API.\n\n\n\n Functionalities in model B: \n\nFile upload: While using Model B for upload, Application uses local Encryption method \nand uploads the file to S3 bucket. The key used to \nEncrypt the file can be uploaded to HSM cluster using \nbelow command.\nimSymKey -f key_name -t 31 -l aes256-imported -w\n\nFile Download: While using Model B for download, \nuser need to give the cluster name and key details. Key can be downloaded \nusing the below command and used for decryption in local \nencryption method.\nexSymKey -k Key_id -out key_file_name_to_save -w"
        label1=tk.Label(self, text=matter, font=('helvetica', 15))
        canvas1.create_window(300,300, window=label1)
       
#upload option page 3
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        def modela():
            controller.fun(Modela_1)
            controller.show_frame("Modela_1")
        def modelb():
            controller.show_frame("pageb")
        def modelc():
            controller.fun(Modelc_1)
            controller.show_frame("Modelc_1")
        def modela_info():
            im = Image.open(r"modela.PNG")
            im.show()
        def modelb_info():
            im = Image.open(r"modelb.PNG")
            im.show()
        def modelc_info():
            im = Image.open(r"modelc.PNG")
            im.show()
        button = tk.Button(self, text="Logout", command=lambda:controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=lambda:controller.show_frame("Decide"))
        canvas1.create_window(575, 30, window=buttona)
        label1=tk.Label(self, text="Select from below Models of Encryption to upload the file", font=('helvetica', 18, 'bold'))
        canvas1.create_window(250,40, window=label1)
        button1 = tk.Button(self, text="\n\n\n   MODEL A   \n\n\n", command=modela)
        canvas1.create_window(130, 180, window=button1)
        button2 = tk.Button(self, text="\n\n\n   MODEL B   \n\n\n", command=modelb)
        canvas1.create_window(230, 180, window=button2)
        button3 = tk.Button(self, text="\n\n\n   MODEL C   \n\n\n", command=modelc)
        canvas1.create_window(330, 180, window=button3)
        button4 = tk.Button(self, text="more info..", command=modela_info)
        canvas1.create_window(130, 250, window=button4)
        button5 = tk.Button(self, text="more info..", command=modelb_info)
        canvas1.create_window(230, 250, window=button5)
        button6 = tk.Button(self, text="more info..", command=modelc_info)
        canvas1.create_window(330, 250, window=button6)

#model a upload page
class Modela_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas1 = tk.Canvas(self, width = 600, height = 600)
        canvas1.pack()
        canvas2 = tk.Canvas(self, width = 300, height = 300)
        canvas2.pack()
        canvas1.create_window(400, 400, window=canvas2)
        canvas3 = tk.Canvas(self, width = 300, height = 300)
        canvas3.pack()
        canvas1.create_window(400, 500, window=canvas3)
        
        def write_key():
            key = Fernet.generate_key()
            with open(key_filename, "wb") as key_file:
                key_file.write(key)
            encryption(filename, key_filename, bucket_name)
        def encryption(input_filename, key_filename, s3bucketname):
            canvas3.delete("all")
            key = open(key_filename, "rb").read()
            f = Fernet(key)
            with open(input_filename, "rb") as file:
                # read all file data
                file_data = file.read()
            # encrypt data
            encrypted_data = f.encrypt(file_data)
            #print("\ninput file data after encryption is " + str(encrypted_data))
            # write the encrypted file
            x=input_filename.split('/')
            file_name=x[len(x)-1]
            with open(file_name, "wb") as file:
                file.write(encrypted_data)
            #---s3 upload
            #s3_client = boto3.client('s3',aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password)
            object_name=file_name
            try:
                client.upload_file(file_name, bucket_name, object_name)
                label3=tk.Label(self, text="Upload Success!!", font=('helvetica', 18, 'bold'))
                canvas3.create_window(0,50,window=label3)
            except Exception as e:
                label3=tk.Label(self, text=e, font=('helvetica', 18, 'bold'))
                canvas3.create_window(0,50,window=label3)
            os.remove(file_name)
        def key():
            global key_filename
            key_filename = filedialog.asksaveasfilename(initialdir = "/",title = "Choose the path and Select a filename for key",filetypes = (('Text Document', '*.txt'),("all files","*.*")))
            disp="file selected to upload:\n"+key_filename
            label2=tk.Label(self, text= disp, fg='black', font=('helvetica', 18, 'bold'))
            canvas2.create_window(0, 0, window=label2)
            button1=tk.Button(self,text="Confirm selection", command=write_key)
            canvas2.create_window(0, 50, window=button1)
        button = tk.Button(self, text="Logout", command=lambda:controller.show_frame("StartPage"))
        canvas1.create_window(575, 10, window=button)
        buttona = tk.Button(self, text="Home", command=lambda:controller.show_frame("Decide"))
        canvas1.create_window(575, 30, window=buttona)
        label1=tk.Label(self, text="Select destination to save key file", font=('helvetica', 18, 'bold'))
        canvas1.create_window(250,40, window=label1)
        button = tk.Button(self, text="select destination", command=key)
        canvas1.create_window(250, 75, window=button)

#model c upload page
class Modelc_1(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            canvas1 = tk.Canvas(self, width = 600, height = 600)
            canvas1.pack()
            canvas2 = tk.Canvas(self, width = 300, height = 300)
            canvas2.pack()
            canvas1.create_window(400, 350, window=canvas2)
            def logout():
                canvas2.delete("all")
                controller.show_frame("StartPage")
            def home():
                canvas2.delete("all")
                controller.show_frame("Decide")
            def upload():
                try:
                    os.system("aws configure set aws_access_key_id '"+access_key_id+"' --profile project")
                    os.system("aws configure set aws_secret_access_key '"+access_key_password+"' --profile project")
                    os.system("aws s3 cp "+filename+" s3://termprojectbucket2020/ --sse aws:kms --sse-kms-key-id "+variable1.get()+" --profile project")
                    labelu=tk.Label(self, text="Upload Success!!", font=('helvetica', 18, 'bold'))
                    canvas2.create_window(0,100, window=labelu)
                except Exception as e:
                    labelu=tk.Label(self, text=e, font=('helvetica', 18, 'bold'))
                    canvas2.create_window(0,100, window=labelu)
            def key():
                canvas2.delete("all")
                try:
                    client = boto3.client('kms',aws_access_key_id=access_key_id, aws_secret_access_key=access_key_password, region_name=text1.get("1.0","end-1c"))
                    response=client.list_keys()
                    collection=[]
                    if response['Keys']!=[]:
                        for key in response['Keys']:
                            collection.append(key['KeyId'])
                        global variable1
                        variable1 = tk.StringVar()
                        variable1.set(collection[0])
                        labelk=tk.Label(self, text="Select from below Key accessible to you:", font=('helvetica', 18, 'bold'))
                        canvas2.create_window(0,0, window=label1)
                        opt = tk.OptionMenu(app, variable1, *collection)
                        canvas2.create_window(0,20, window=opt)
                        buttonu=tk.Button(self, text="Upload", command=upload)
                        canvas2.create_window(0, 60, window=buttonu)
                    else:
                        labelk=tk.Label(self, text="No Keys in selected region are accessible to you:", font=('helvetica', 18, 'bold'))
                        canvas2.create_window(0,0, window=labelk)
                except Exception as e:
                    labelk=tk.Label(self, text=e, font=('helvetica', 18, 'bold'))
                    canvas2.create_window(0,0, window=labelk)
            button = tk.Button(self, text="Logout", command=logout)
            canvas1.create_window(575, 10, window=button)
            buttona = tk.Button(self, text="Home", command=home)
            canvas1.create_window(575, 30, window=buttona)
            label1=tk.Label(self, text="Enter region to select KMS", font=('helvetica', 18))
            canvas1.create_window(200,50, window=label1)
            text1=tk.Text(self,height=1,width=20)
            canvas1.create_window(200, 80, window=text1)
            text1.insert(tk.INSERT,"Key-path")
            button = tk.Button(self, text="List KMS", command=key)
            canvas1.create_window(200, 120, window=button)
            


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
