from multiprocessing import context
from django.shortcuts import render, redirect
#from medcare.decorators import login_required_redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django import forms
from django.core.files.storage import default_storage
from django.urls import reverse
import os
import shutil
from django.conf import settings
from .forms import DiabetesInputForm, AIDsInputForm
import random, cv2
from django.core.files.base import ContentFile
from io import BytesIO

# Create your views here.

def gotoecg(request):
    return render(request, "diseaseprediction/predict_ecg.html")

def gotocataract(request):
    return render(request, "diseaseprediction/predict_cataract.html")

def gotostress(request):
    return render(request, "diseaseprediction/predict_stress.html")

def gototubersulosis(request):
    return render(request, "diseaseprediction/predict_tubersulosis.html")

def gototumor(request):
    return render(request, "diseaseprediction/predict_tumor.html")

def gotodiabetes(request):
    return render(request, "diseaseprediction/predict_diabetes.html", {"form": DiabetesInputForm()})

def gotoaids(request):
    return render(request, "diseaseprediction/predict_aids.html",{'form': AIDsInputForm()})

def home_diseaseprediction(request):
    return render(request, 'diseaseprediction/home_diseaseprediction.html')

def about_us(request):
    return redirect(reverse('aboutUs'))

def login_u(request):
    return redirect(reverse('login'))


#from .ai_models.cataract_model import cataract
from .models import MyModel  # Import the model from models.py
#import torchvision.transforms as tt
import os
import logging
import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as tt

class MyForm(forms.Form):
    image = forms.ImageField()


def ecg_image2tensor(image_path):
    model_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\diseaseprediction\aimodels\CS_Net.pt" 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    Model = torch.jit.load(model_path, map_location=device)
    Model.eval()

    transform = tt.Compose(
    [
        tt.Resize((288,288)),
        tt.Grayscale(num_output_channels=1),
        tt.ToTensor()
    ]
)

    img = Image.open(image_path)
    img = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = Model(img)
        print(pred)
        #pred = torch.sigmoid(pred).item()
        result = torch.argmax(pred, dim=1)
        result = result.item()
        print(f"Prediction: {result} ")
    return str(result)

def predict_ecg(request):
    if request.method == "POST" and request.FILES.get('image'):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():

            uploaded_image = request.FILES['image']
            file_path = default_storage.save(f"uploads/{uploaded_image.name}", uploaded_image)
            try:
                image_instance = MyModel(image=uploaded_image)
                image_instance.save()

                image_path = image_instance.image.path
                logging.basicConfig(level=logging.INFO)
                logging.info(f"Image saved at: {image_path}")  
                if not os.path.exists(image_path):
                    logging.error("ERROR: File was not saved!")
                    return JsonResponse({"error": "File was not saved!"}, status=500)

                result = ecg_image2tensor(image_path)  
                #return render(request, "hello/disease_result.html", {"result": "You have a cataract problem" if result else "You don't have a cataract problem"})
                #return render(request, 'hello/disease_result.html',{"result": "You have a cataract problem" if result else "You don't have a cataract problem"})
                #return render(request, 'hello/disease_result.html',{"result": result})
                return render(request, "diseaseprediction/result_ecg.html", {'image_url':image_instance.image.url, 'result': result})  # Pass image URL to template

    
            except Exception as e:
                logging.error(f"Error: {e}")
                return JsonResponse({"error": f"Error: {e}"}, status=500)

    return JsonResponse({"error": "Invalid Request"}, status=400)

def feedback_ecg(request):
    return redirect(home_diseaseprediction)
"""def feedback_ecg(request, result, path):
    original_path = os.path.join(settings.MEDIA_ROOT, path)
    feedback_dir = os.path.join(settings.MEDIA_ROOT, 'feedback_ecg', result)
    os.makedirs(feedback_dir, exist_ok=True)
    filename = os.path.basename(original_path)
    new_path = os.path.join(feedback_dir, filename)
    
    try:
        shutil.move(original_path, new_path)
        # Construct the relative path for the image URL


        new_relative_path = os.path.join('feedback_ecg', result, filename).replace('\\', '/')
        return render(request, "diseaseprediction/result_ecg.html", {
            "image_url": new_relative_path, 
            'result': result
        })
    except Exception as e:
        return JsonResponse({"message": f"Error: {str(e)}", "status": "error"})"""

def feedback_cataract(request):
    return render(request, "diseaseprediction/feedback_cataract.html")

"""def feedback_cataract(request, result, path):
    original_path = os.path.join(settings.MEDIA_ROOT, path)
    feedback_dir = os.path.join(settings.MEDIA_ROOT, 'feedback_ecg', result)
    os.makedirs(feedback_dir, exist_ok=True)
    filename = os.path.basename(original_path)
    new_path = os.path.join(feedback_dir, filename)
    
    try:
        shutil.move(original_path, new_path)
        # Construct the relative path for the image URL
        
        if result == 'Cataract':
            result = '0'
        else:
            result = '1'
        new_relative_path = os.path.join('feedback_cataract', result, filename).replace('\\', '/')
        return render(request, "diseaseprediction/result_cataract.html", {
            "image_url": new_relative_path, 
            'feedback': "Thanks for the feedback",
            'path':'jifdj'
        })
    except Exception as e:
        return JsonResponse({"message": f"Error: {str(e)}", "status": "error"})"""

def cataract_image2tensor(image_path):
    
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "ai_models", "cataract3.pt")
    print(f"🔍 Checking Model Path: {MODEL_PATH}")
    #if not os.path.exists(MODEL_PATH):
    #    raise FileNotFoundError(f"Error: Model file not found at {MODEL_PATH}") 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    Model = torch.jit.load(r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\diseaseprediction\aimodels\cataract.pt",map_location=device)
    Model.eval()

    transform = tt.Compose([
        tt.Resize((256, 256)),
        tt.CenterCrop(256),
        tt.ToTensor()
    ])

    img = Image.open(image_path).convert('RGB')  # Open Image
    img = transform(img).unsqueeze(0).to(device)  # Apply transformation
    with torch.no_grad():
        pred = Model(img)
        print(pred)
        #pred = torch.sigmoid(pred).item()
        label = "Cataract" if pred > 0.5 else "Normal"
        print(f"Prediction: {label} ")
    return label

def predict_cataract(request):
    if request.method == "POST" and request.FILES.get('image'):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():

            uploaded_image = request.FILES['image']
            file_path = default_storage.save(f"uploads/{uploaded_image.name}", uploaded_image)
            try:
                image_instance = MyModel(image=uploaded_image)
                image_instance.save()

                image_path = image_instance.image.path
                logging.basicConfig(level=logging.INFO)
                logging.info(f"Image saved at: {image_path}")  
                if not os.path.exists(image_path):
                    logging.error("ERROR: File was not saved!")
                    return JsonResponse({"error": "File was not saved!"}, status=500)

                result = cataract_image2tensor(image_path)  
                
                return render(request, "diseaseprediction/predict_cataract.html", {'result': result, 'image':image_instance.image.url})
            except Exception as e:
                logging.error(f"Error: {e}")
                return JsonResponse({"error": f"Error: {e}"}, status=500)
        else:
            return JsonResponse({"error": "Invalid form"}, status=400)

    return JsonResponse({"error": "Invalid Request"}, status=400)

def tb_image2tensor(image_path):
    model_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\diseaseprediction\aimodels\DC_Net.pt" 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    Model = torch.jit.load(model_path, map_location=device)
    Model.eval()

    transform = tt.Compose(
    [
        tt.Resize((256,256)),
        tt.CenterCrop((256,256)),
        tt.ToTensor()
    ]
)

    img = Image.open(image_path)  # Open Image
    img = transform(img).unsqueeze(0).to(device)  # Apply transformation
    with torch.no_grad():
        pred = Model(img)
        #pred = torch.sigmoid(pred).item()
        label = 'tuberculosis' if pred>0.5 else 'no turebculosis'
        print(f"Prediction: {label,pred} ")
        return label

def predict_tuberculosis(request):
    if request.method == "POST" and request.FILES.get('image'):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid(): 

            uploaded_image = request.FILES['image']
            try:
                image_instance = MyModel(image=uploaded_image)
                image_instance.save()

                image_path = image_instance.image.path
                print(image_path)
                #logging.basicConfig(level=logging.INFO)
                #logging.info(f"Image saved at: {image_path}")  
                if not os.path.exists(image_path):
                    logging.error("ERROR: File was not saved!")
                    return JsonResponse({"error": "File was not saved!"}, status=500)

                result = tb_image2tensor(image_path)  
                
                return render(request, "diseaseprediction/predict_tubersulosis.html", {'result': result , 'image_path':image_instance.image.url})
            except Exception as e:
                logging.error(f"Error: {e}")
                return JsonResponse({"error": f"Error: {e}"}, status=500)
        else:
            return JsonResponse({"error": "Invalid form"}, status=400)

    return JsonResponse({"error": "Invalid Request"}, status=400)

def diabetes_form2tensor(form_data):
    model_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\diseaseprediction\aimodels\diabetes.pt" 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    Model = torch.jit.load(model_path, map_location=device)
    Model.eval()
    cleaned_data = torch.tensor([list(form_data.values())]).to(device)

    pred = Model(cleaned_data)
    print(pred)
    return pred
    
def predict_diabetes(request):
    result = None  # Default result when the page loads
    if request.method == 'POST':
        form = DiabetesInputForm(request.POST)
        if form.is_valid():
            # Retrieve cleaned data from the form
            data = form.cleaned_data
            
            result = diabetes_form2tensor(data)

            if result > 0.5:
                result1 = "Higher risk detected. Please consult with a healthcare professional for further evaluation and guidance."
            else:
                result1 = "No risk detected. Maintain healthy habits and consider regular check-ups to monitor your health."
        else:
            # Optionally, you can log form.errors or handle invalid form data
            pass
    else:
        form = DiabetesInputForm()

    context = {
        'form': form,
        'result': result1,
    }
    return render(request, 'diseaseprediction/predict_diabetes.html', context)


def tumor_image2image(img_path, uploaded_filename):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_path = r"C:\Users\GANAPATHI\Desktop\NIT\project\ymhhacakthon\medcare\diseaseprediction\aimodels\tumor.pt"

    # Load model
    model = torch.jit.load(model_path, map_location=device)
    model.to(device)
    model.eval()

    # Load and preprocess input image
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    image = torch.from_numpy(image).float().unsqueeze(0).permute(0, 3, 1, 2).to(device)

    # Inference
    with torch.no_grad():
        output = model(image)
    output = (output > 0.5).float()

    # Convert to PIL Image
    img_tensor = output.squeeze(0).squeeze(0).detach().cpu()
    output_img = (img_tensor.numpy() * 255).astype('uint8')
    output_pil = Image.fromarray(output_img)

    # Convert PIL to Django ImageField-compatible file
    buffer = BytesIO()
    output_pil.save(buffer, format='PNG')
    image_png = buffer.getvalue()
    buffer.close()

    # Save to Django model
    result_filename = "result_" + os.path.basename(uploaded_filename)
    instance = MyModel()
    instance.image.save(result_filename, ContentFile(image_png))
    instance.save()

    print(f"✅ Saved output image to: {instance.image.path}")
    return instance.image.url 



def predict_tumor(request):
    if request.method == "POST" and request.FILES.get('image'):
        form = MyForm(request.POST, request.FILES)
        if form.is_valid(): 

            uploaded_image = request.FILES['image']
            try:
                image_instance = MyModel(image=uploaded_image)
                image_instance.save()

                image_path = image_instance.image.path
                print(image_path)
                #logging.basicConfig(level=logging.INFO)
                #logging.info(f"Image saved at: {image_path}")  
                if not os.path.exists(image_path):
                    logging.error("ERROR: File was not saved!")
                    return JsonResponse({"error": "File was not saved!"}, status=500)

                result = tumor_image2image(image_path, uploaded_image.name)  
                context = {
                    'uploaded_image_url': image_instance.image.url,
                    'result_image_url': result
                    }
                print(context)

                return render(request, "diseaseprediction/predict_tumor.html", context)
            except Exception as e:
                logging.error(f"Error: {e}")
                return JsonResponse({"error": f"Error: {e}"}, status=500)
        else:
            return JsonResponse({"error": "Invalid form"}, status=400)

    return JsonResponse({"error": "Invalid Request"}, status=400)



def aids_form2tensor(form_data):
    pass

def predict_aids(request):
    result = None  # Default result is None until a prediction is made.
    
    if request.method == 'POST':
        form = AIDsInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # For simulation, use the submitted chronological age.
            age = data.get('age')
            # Simulate a predicted biological age by adding a random fluctuation.
            predicted_age = age + random.uniform(-5, 5)
            age_diff = predicted_age - age
            
            if age_diff > 2:
                result = (
                    f"Your predicted biological age is {predicted_age:.1f} years. "
                    f"This is {age_diff:.1f} years older than your chronological age. "
                    "Consider lifestyle modifications to improve your biomarkers."
                )
            elif age_diff < -2:
                result = (
                    f"Your predicted biological age is {predicted_age:.1f} years. "
                    f"This is {abs(age_diff):.1f} years younger than your chronological age. "
                    "Your biomarkers indicate good biological health."
                )
            else:
                result = (
                    f"Your predicted biological age is {predicted_age:.1f} years, "
                    "which closely matches your chronological age."
                )
    else:
        form = AIDsInputForm()

    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'diseaseprediction/predict_aids.html', context)



def index(request):
    return render(request, "hello/disease_prediction.html", {'form': MyForm()})




