# Text-to-Image Generator using Hugging Face and Streamlit

A simple and interactive web app that generates images from text descriptions using the Hugging Face API and Streamlit.

## 🛠️ Features
- **Text-to-Image Generation**: Enter a caption or description, and the app generates an image based on the input.
- **Hugging Face API Integration**: Uses the `black-forest-labs/FLUX.1-dev` model hosted on Hugging Face to convert text to images.
- **Simple and Clean UI**: Built using Streamlit, providing a smooth user experience.

## 🌐 Live Demo
Check out the live demo here (link to your live app).

## 💡 How It Works
1. The user enters a description in the text area (e.g., "A scenic mountain view at sunset").
2. The description is sent to the Hugging Face model via an API request.
3. The model generates an image based on the description.
4. The generated image is displayed on the page.

## 🚀 Installation

### Prerequisites
- Python 3.x
- A Hugging Face account (to generate an API key)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/text-to-image-generator.git
   cd text-to-image-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your Hugging Face API key:
   ```
   HF_API_KEY=your_hugging_face_api_key
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 🧑‍💻 Code Explanation

- **`extract_keywords`**: A mock function that processes the input caption and returns the extracted keywords. (This can be customized based on your requirements).
- **`generate_image`**: Sends the extracted keywords to the Hugging Face API to generate the image and returns the image.
- **Streamlit UI**: The UI includes a text area for user input and a button to trigger image generation. The image is displayed on successful generation.

## 📦 Dependencies
- `requests`: To make API calls to Hugging Face.
- `python-dotenv`: To load environment variables.
- `Pillow`: For image processing and displaying the generated image.
- `streamlit`: For building the interactive web app.

## 🤝 Contributing
If you want to contribute, feel free to fork the repository and create a pull request. You can also report any issues or suggest improvements. Feel free to reach out to me for discussions !

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
