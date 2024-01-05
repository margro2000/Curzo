import requests 
import json
from knowledge_service import search_embeddings

class chat_content:
    def __init__(self, client_id, client_secret, resource, grant_type, model):
        self.tenantId = "72f988bf-2d7cd011db47"
        self.auth_url = "https://login.microsoftonline.com/" + self.tenantId + "/oauth2/token" 
        self.client_id = client_id 
        self.client_secret = client_secret
        self.resource = resource
        self.grant_type = grant_type
        self.model = model

    def get_context(self, id, user_query):
            # Use the search_embeddings function to get a list of document names matching the user query
            context = search_embeddings(user_query, id, top_n=3)

            # If there are no results, return an empty string
            if not context:
                return "No context found"

            # Otherwise, return the first result as the context
            return context


    def get_chat_response(self, user_query):
        data = { 
        "grant_type": self.grant_type, 
        "client_id": self.client_id, 
        "client_secret": self.client_secret, 
        "resource": self.resource 
        }

        auth_response = requests.post(self.auth_url, data=data) 
        authjson = auth_response.content 
        authdata = json.loads(authjson) 
        token = (authdata['access_token'])  
        head = {"Authorization": "Bearer " + token} 
        # context = "Albert Einstein was born on March 14, 1879, in Ulm, Germany. He grew up in a middle-class Jewish family in Munich. As a child, Einstein became fascinated by music, mathematics, and science. He dropped out of school at 16 and eventually enrolled at the Swiss Federal Institute of Technology in Zurich, where he graduated in 1900. In 1905, Einstein published four groundbreaking papers, which were later called the 'Annus Mirabilis' or 'Miracle Year' papers. These papers revolutionized the field of physics, introducing the theory of relativity, explaining the photoelectric effect, and providing evidence for the existence of atoms. In 1915, Einstein published the general theory of relativity, which expanded on his earlier work and proposed that gravity is the curvature of spacetime caused by mass. This theory was confirmed during the solar eclipse of 1919, making Einstein an international celebrity. In 1921, Einstein was awarded the Nobel Prize in Physics for his explanation of the photoelectric effect, though many believe he should have received it for his work on relativity. As the political situation in Germany deteriorated in the 1930s, Einstein, who was of Jewish descent, decided to leave the country. He accepted a position at the Institute for Advanced Study in Princeton, New Jersey, where he worked until his death in 1955. While at Princeton, Einstein continued to work on various aspects of physics, including the search for a unified field theory that would combine all the forces of nature into a single, coherent framework. He also became increasingly involved in political and social issues, advocating for nuclear disarmament, civil rights, and world government. Albert Einstein passed away on April 18, 1955, leaving behind a legacy of groundbreaking scientific contributions and a commitment to peace and social justice."
        context = self.get_context(user_query)

        system_message = """You are a helpful assistant that can answer questions about the wiki information provided by the user. You must 
                            provide a step-by-step process whenever is necessary. You must only provide answers when the sources contain it.
                        """
        
        content = f"""Given: {context}.\nPlease answer the following question: {user_query} and provide a link to more."""

        r = requests.post('https://iks-ppe.ideas.microsoft.com/api/odata/v1.0.0/OpenAIChatCompletions/Create', 
                          headers=head, 
                          json={
                              "Request": {
                                  "Model": self.model,
                                  "Body": {
                                      "Messages": [
                                          {"Role": "System", "Content": system_message},
                                          {"Role": "User", "Content": content}
                                      ],
                                      "Temperature": 0.2,
                                      "Max_tokens": 1500,
                                      "Top_p": 1,
                                      "Presence_penalty": 0.0,
                                      "Frequency_penalty": 0.0
                                  }
                              }
                          })

        response = json.loads(r.content)
        choices = response["Choices"]
        for choice in choices:
            content = choice["Message"]["Content"]
            return content
        

if __name__ == "__main__":
    client_id = "db7bea3e-7c8b-43d1-869d-53" 
    client_secret = "f898Q~L_cAKM7HsCvaXEsI5t5caw"
    resource = "api://db9378b4-8fc2-12f5fd"
    grant_type = "client_credentials"
    model = "gpt-35-turbo"

    chat = chat_content(client_id, client_secret, resource, grant_type, model)
    user_query = "What was Albert known for, and what was he liked or hated by humans?"
    response = chat.get_chat_response(context, user_query)
    print(response)