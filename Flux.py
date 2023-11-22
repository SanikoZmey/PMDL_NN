import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
import torchvision.transforms as T
import torchvision.transforms.functional as F

from model_arch import ResNet, Alex_like

@st.cache_resource
def load_model(model_type: str):
    if(model_type == "AlexNet-like"):
        model = Alex_like(num_classes=26)
        model.load_state_dict(torch.load('./runs/Alex_Like.pt'))
    else:
        model = ResNet(num_classes=26)
        model.load_state_dict(torch.load('./runs/ResNet34.pt'))
    
    model.eval()
    return model

@st.cache_data
def load_class_dict():
    with open("classes_dict.txt", "r") as class_dict:
        return eval(class_dict.read())

def preprocess_image(image):
    transforms = T.Compose([
        T.Resize(size=(200, 200)),
        T.ToTensor(),
    ])

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image[228:855,64:1856]
    image = Image.fromarray(image)
    image = transforms(image)
    image = F.adjust_sharpness(image, 4.5)
    image = image.numpy()[np.newaxis, :, :, :]

    image = torch.tensor(image)

    return image

def predict(image, model) -> torch.tensor:    
    with torch.no_grad():
        pred_class = model(image).argmax(dim=1, keepdim=True)
    return pred_class

if __name__ == '__main__':
    st.title('Flux - NN for recognition of simplified movements of a VR controller')
    class_dict = load_class_dict()
    
    option = st.selectbox(
        'Which model do you want to use for predictions?',
        ('ResNet34', 'AlexNet-like'), 
        index=None,
        placeholder="Select the model"
    )

    if(option is not None):
        st.markdown(f'''You selected :orange[{option} model] for predictions''')

        with st.form("Files_to_recognise", clear_on_submit=True):
            upl_images = st.file_uploader("Now choose files for a recognition", accept_multiple_files=True)
            submitted = st.form_submit_button("Recognise")

            if submitted and upl_images is not None:
                images_to_show, captions = [], []
                model = load_model(option)

                for upl_image in upl_images:
                    file_bytes = np.asarray(bytearray(upl_image.read()), dtype=np.uint8)
                    image = cv2.imdecode(file_bytes, 1)
                    image = preprocess_image(image)
                    images_to_show.append(np.squeeze(image.numpy()))           

                    pred_class = predict(image, model).item()

                    captions.append(class_dict[pred_class + 1])
                
                st.text("Here are the movements and their predicted classes")
                st.image(images_to_show, captions)    
        