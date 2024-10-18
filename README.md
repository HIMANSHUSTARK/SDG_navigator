
# HealthWise AI - Your Personal Health Explanation Assistant

## Overview

*HealthWise AI* is an innovative health technology application designed to empower individuals by simplifying complex medical information. Utilizing the capabilities of OpenAI's GPT-4o-mini API, the app translates medical jargon into easy-to-understand language. It helps users comprehend their health conditions, medical reports, and treatment options without the need for fine-tuning the AI model.

## Inspiration

The inspiration for HealthWise AI came from witnessing the confusion and anxiety that often accompany medical diagnoses. Many people struggle to understand their health conditions due to the complexity of medical terminology. We wanted to create a tool that bridges the communication gap between healthcare professionals and patients, making health information more accessible and less intimidating.

## What We Learned

Throughout the development of HealthWise AI, we learned:

- *The Power of Prompt Engineering*: Crafting effective prompts is crucial to guide the AI in providing accurate and helpful responses.
- *User Privacy is Paramount*: Implementing strong data protection measures is essential to maintain user trust.
- *Ethical AI Use*: It's important to balance providing helpful information with encouraging users to seek professional medical advice.

## How We Built the Project

### Technology Stack

- *Frontend*: [Streamlit](https://streamlit.io/) for creating an interactive and user-friendly interface.
- *Backend*: Python, utilizing OpenAI's GPT-4 API for natural language processing.
- *Libraries*: [LangChain](https://langchain.readthedocs.io/) for efficient prompt management.

### Development Steps and Importance

1. *User Input Interface*

   - *What We Did*: Developed a simple interface where users can input medical terms, diagnoses, or symptoms.
   - *Importance*: Ensures accessibility for users of all tech proficiency levels.
   - *Associated SDG: *Goal 3: Good Health and Well-being - Promoting health literacy.

2. *Prompt Engineering*

   - *What We Did*: Crafted prompts to guide GPT-4 in generating clear and accurate explanations.
   - *Importance*: Enhances the reliability and usefulness of the information provided.
   - *Associated SDG: *Goal 4: Quality Education - Ensuring inclusive and equitable quality education.

3. *AI Integration*

   - *What We Did*: Integrated GPT-4 API to process inputs and generate user-friendly responses.
   - *Importance*: Leverages cutting-edge AI to simplify complex medical jargon.
   - *Associated SDG: *Goal 9: Industry, Innovation, and Infrastructure - Fostering innovation.

4. *Privacy Measures*

   - *What We Did*: Implemented data encryption and ensured no user data is stored.
   - *Importance*: Protects user confidentiality and builds trust.
   - *Associated SDG: *Goal 16: Peace, Justice, and Strong Institutions - Promoting just and inclusive societies.

## Key Features and Their Importance

### Medical Jargon Simplification

- *Feature*: Users can input medical terms or excerpts from reports to receive simplified explanations.
- *Importance*: Makes health information accessible to non-medical individuals.
- *Associated SDG: *Goal 3: Good Health and Well-being.

### Personalized Health Insights

- *Feature*: Provides general information about health conditions and lifestyle suggestions.
- *Importance*: Empowers users to make informed health decisions.
- *Associated SDG: *Goal 3: Good Health and Well-being.

### Symptom Checker

- *Feature*: Users describe symptoms to receive potential explanations.
- *Importance*: Encourages proactive health management.
- *Associated SDG: *Goal 3: Good Health and Well-being.

### Privacy-Focused Design

- *Feature*: Ensures data encryption and non-storage of user data.
- *Importance*: Upholds privacy and builds user trust.
- *Associated SDG: *Goal 16: Peace, Justice, and Strong Institutions.

## Challenges Faced

1. *Ensuring Accuracy*

   - *Challenge*: Crafting prompts to avoid misinformation.
   - *Solution*: Iterative testing and refining of prompts.
   - *Importance*: Maintains the reliability of the app.

2. *Ethical Considerations*

   - *Challenge*: Avoiding the provision of definitive medical advice.
   - *Solution*: Including disclaimers and encouraging professional consultations.
   - *Importance*: Ensures responsible use of AI.

3. *Data Privacy*

   - *Challenge*: Protecting sensitive user information.
   - *Solution*: Implementing robust encryption and not storing data.
   - *Importance*: Complies with data protection standards.

## Potential Impact

HealthWise AI aims to:

- *Improve Health Literacy*: By making medical information accessible.
- *Empower Users*: To engage actively in health management.
- *Reduce Healthcare Disparities*: Through accessible health education.
- *Align with Social Good*: Supporting public health outcomes.

## Alignment with Sustainable Development Goals (SDGs)

- *Goal 3: Good Health and Well-being*

  - Promotes health literacy and empowers individuals.

- *Goal 4: Quality Education*

  - Provides accessible education on health topics.

- *Goal 9: Industry, Innovation, and Infrastructure*

  - Utilizes innovative technology to enhance healthcare access.

- *Goal 16: Peace, Justice, and Strong Institutions*

  - Ensures ethical standards and privacy, fostering trust.

## Conclusion

HealthWise AI leverages the power of GPT-4o-mini to simplify complex medical information, making healthcare more accessible and less daunting. By focusing on user-centric design and ethical AI practices, it stands as a promising tool with real-world impact, contributing to a more informed and healthier society.

---

By bridging the gap between medical professionals and patients, HealthWise AI not only demystifies health information but also supports individuals in making informed health decisions


How to Run HealthWise AI
------------------------

### Prerequisites

Before running the application, ensure the following dependencies are installed:

*   **Python 3.8 or higher**
    
*   **Streamlit** for building the web interface
    
*   **LangChain** for conversation management
    
*   **OpenAI Python SDK** for integrating with GPT-4o-mini
    
*   **dotenv** (optional) for handling environment variables  `
Install the required dependencies using the requirements.txt file or the following command:
```
pip install streamlit langchain openai python-dotenv
```
### 1\. **Clone the Repository**

First, clone the repository and navigate to the project directory:
```
 git clone https://github.com/HIMANSHUSTARK/SDG_navigator.git  
 cd SDG_navigator   `
```
### 2\. **Set Up OpenAI API Key**
To access OpenAI's GPT-4o-mini, you need to set your API key. Create a .env file in the project root with the following content:
```
OPENAI_API_KEY=your_openai_api_key
```
Alternatively, you can directly set the key in the script by replacing:
```
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
```
### 3\. **Run the Application**
To start the Streamlit app, use the following command:
```
streamlit run health1.py
```
### 4\. **Usage**

*   The web interface will open, allowing you to interact with the Healthcare Assistant.
    
*   Input medical terms, symptoms, or questions to receive simplified explanations.
    
*   The conversation history is maintained throughout the session, and you have the option to save it.
    

### 5\. **Saving Chat History**

The chat history can be saved at any time by clicking the **Save Chat History** button, and the file will be saved in the format ```chat\_history\_YYYYMMDD\_HHMMSS.txt```.
### Dependencies

Make sure the following dependencies are listed in your ```requirements.txt```:
```
streamlit==1.25.0
langchain==0.16.0
openai==0.27.2
python-dotenv==1.0.0
```

Here are Examples of how the interface looks:
![hl chatbot](https://github.com/user-attachments/assets/be98c851-ae92-4185-a9e9-4c1b6e714cb9)

------
------
![healtcare chatbot](https://github.com/user-attachments/assets/ef379d44-53a1-4a58-962c-9c37b2c97587)
