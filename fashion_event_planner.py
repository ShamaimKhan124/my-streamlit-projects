import streamlit as st
import os
from PIL import Image


outfits = {
    "Wedding": {
        "Men": {
            "style": "Classic suit or sherwani",
            "accessories": ["Tie or pocket square", "Leather shoes", "Watch"],
            "image": "outfits/wedding_men.jpg"
        },
        "Women": {
            "style": "Elegant gown or traditional attire",
            "accessories": ["Diamond earrings", "Clutch bag", "Heels"],
            "image": "outfits/wedding_women.jpg"
        }
    },
    "Party": {
        "Men": {
            "style": "Stylish blazer with jeans",
            "accessories": ["Casual sneakers", "Leather bracelet", "Sunglasses"],
            "image": "outfits/party_men.jpg"
        },
        "Women": {
            "style": "Cocktail dress or trendy outfit",
            "accessories": ["Statement necklace", "Handbag", "High heels"],
            "image": "outfits/party_women.jpg"
        }
    },
    "Business Meeting": {
        "Men": {
            "style": "Formal suit with dress shoes",
            "accessories": ["Tie", "Briefcase", "Leather watch"],
            "image": "outfits/business_men.jpg"
        },
        "Women": {
            "style": "Formal blazer with trousers or a pencil skirt",
            "accessories": ["Handbag", "Stud earrings", "Heels"],
            "image": "outfits/business_women.jpg"
        }
    },
    "Casual Outing": {
        "Men": {
            "style": "Jeans with a polo shirt",
            "accessories": ["Sneakers", "Backpack", "Sunglasses"],
            "image": "outfits/casual_men.jpg"
        },
        "Women": {
            "style": "Jeans & stylish top",
            "accessories": ["Crossbody bag", "Flats", "Sunglasses"],
            "image": "outfits/casual_women.jpg"
        }
    }
}


st.title("👗👔 Fashion Event Outfit Planner")
st.write("Select an event and gender to get outfit recommendations!")


event = st.selectbox("🎉 Choose your event:", list(outfits.keys()))


gender = st.radio("👤 Select your gender:", ["Men", "Women"])

if event and gender:
    outfit = outfits[event][gender]

    
    st.subheader(f"✨ Recommended Outfit for {event} ({gender}):")
    st.write(f"**Style:** {outfit['style']}")

    
    st.write("👜 **Matching Accessories:**")
    for acc in outfit["accessories"]:
        st.write(f"- {acc}")

    
    image_path = outfit["image"]
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"{event} Outfit ({gender})", use_container_width=True)
    else:
        st.write("🚫 Image not found! Please add an image in the outfits/ folder.")


st.write("---")
st.title("🎨 Color Coordination Guide")
st.write("Select your outfit color to see the best matching combinations!")


color_guide = {
    "Red": ["Gold", "Black", "White"],
    "Blue": ["White", "Silver", "Beige"],
    "Green": ["Brown", "White", "Navy"],
    "Black": ["White", "Red", "Gold"],
    "White": ["Black", "Navy", "Pastels"],
    "Yellow": ["Blue", "Brown", "Green"],
    "Pink": ["Grey", "White", "Beige"],
    "Purple": ["Gold", "Silver", "Black"],
}


selected_color = st.selectbox("👕 Choose your outfit color:", list(color_guide.keys()), key="color_guide")


if selected_color:
    matching_colors = color_guide[selected_color]
    
    st.subheader(f"✨ Best Matching Colors for {selected_color}:")
    
    
    for color in matching_colors:
        st.markdown(
            f'<div style="display: flex; align-items: center; margin-bottom: 5px;">'
            f'<div style="width: 30px; height: 30px; background-color: {color.lower()}; '
            f'margin-right: 10px; border-radius: 50%; border: 1px solid #ccc;"></div>'
            f'<span style="font-size: 18px;">{color}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

st.write("📸 **Want to upload your own outfit?** Upload below!")

uploaded_file = st.file_uploader("Upload your outfit image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Outfit", use_container_width=True)
