from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updaate the public instance attribute
        update_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
         returns a dictionary containing
         all keys/values of __dict__ of the instance
        """
        self.obj_dict = self.__dict__.copy()
        self.obj_dict['__class__'] = self.__class__.__name__
        self.obj_dict['created_at'] = self.created_at.isoformat()
        self.obj_dict['updated_at'] = self.updated_at.isoformat()

        return self.obj_dict
