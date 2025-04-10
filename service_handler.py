from typing import Dict, Any
from datetime import datetime
import uuid

class ServiceRequest:
    def __init__(self, issue_text: str, classification: str, source: str):
        self.request_id = str(uuid.uuid4())
        self.issue_text = issue_text
        self.classification = classification
        self.source = source
        self.timestamp = datetime.now()
        self.status = "New"
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "request_id": self.request_id,
            "issue_text": self.issue_text,
            "classification": self.classification,
            "source": self.source,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status
        }

class ServiceRequestHandler:
    def __init__(self):
        self.requests: Dict[str, ServiceRequest] = {}
        
    def create_request(self, issue_text: str, classification: str, source: str) -> ServiceRequest:
        """
        Create a new service request
        """
        request = ServiceRequest(issue_text, classification, source)
        self.requests[request.request_id] = request
        return request
    
    def get_request(self, request_id: str) -> ServiceRequest:
        """
        Retrieve a service request by ID
        """
        return self.requests.get(request_id)
    
    def update_request_status(self, request_id: str, new_status: str) -> bool:
        """
        Update the status of a service request
        """
        if request_id in self.requests:
            self.requests[request_id].status = new_status
            return True
        return False 