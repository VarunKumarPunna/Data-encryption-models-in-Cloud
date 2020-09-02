# Implementation of Data Encryption models in AWS Cloud

This is the Github repo for the project implementing different models of data encryption - ranging from entirely automated AWS encryption solutions to manual, client-side customizable options.

### Different models of encryption:

**Model A:** Local Encryption & Decryption methods, key storage and key management also needs to be handled by user

**Features of this model:**
- Full control
- Highly customizable
- Needs more effort to build and maintain

**Model B:** Key storage is handled by AWS CloudHSM whereas key management, Encryption & Decryption methods are handled by user 

**Features of this model:**
- Highly secure
- Moderately customizable 
- Costly

**Model C:** Encryption & Decryption methods, key storage and key management are completely handled by AWS KMS service

**Features of this model:**
- Highly secure
- Limited customizability
- Ready to use service

### Steps for using the Application:

1. Copy the project folder into any desired folder in your machine
2. Unzip/Extract the contents into the same folder
3. Open terminal/command prompt and navigate to the unzipped project folder
4. Execute python AWS_project.py
