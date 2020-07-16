from cloudant.client import Cloudant
import mimetypes
import io


API_KEY = {
  "apikey": "ao7tLVel9Ms4WaFe0gXrGXYlvPZ4o3oqm9C8E0O3r3x3",
  "host": "3f867ad1-b1df-471c-935a-5bafbeb180c4-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key b213f645-1734-42d5-9988-55a7099110dc",
  "iam_apikey_name": "MVPkey",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/4bde1a5977a349e4b2943360ec53eae4::serviceid:ServiceId-357ed28e-4a5c-4ed2-bd81-c5ae900e74bc",
  "url": "https://3f867ad1-b1df-471c-935a-5bafbeb180c4-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "3f867ad1-b1df-471c-935a-5bafbeb180c4-bluemix"
}


class Assignment:
    def __init__(self, _id, title, text, due_date, completed=False):
        self._id = _id
        self.title = title
        self.text = text
        self.due_date = due_date
        self.completed = completed
        self.document_ref = None

    def get_data(self):
        return {
            "_id": self._id,
            "Title": self.title,
            "Text": self.text,
            "Due Date": self.due_date,
            "Completed": self.completed
        }


class Database:
    def __init__(self, username, apikey):
        self.client = Cloudant.iam(username, apikey, connect=True)
        self.database = self.client['ibh']


    def disconnect(self):
        self.client.disconnect()


    def create_assignment(self, assignment):
        return self.database.create_document(assignment.get_data())


    def list_assignments(self):
        db_assignments = self.database.all_docs()['rows']
        assignment_ids = list(map(lambda x: x['id'], db_assignments))
        return assignment_ids


    def get_assignments(self):
        assignments = []
        for assignment in self.list_assignments():
            asn = self.database[assignment]
            asn_obj = Assignment(asn['_id'], asn['Title'], asn['Text'],
                                 asn['Due Date'], asn['Completed'])
            asn_obj.document_ref = self.database[assignment]
            assignments.append(asn_obj)

        return assignments


    def add_attachment(self, assignment, path, name):
        with open(path, "rb") as f:
            content_type = mimetypes.MimeTypes().guess_type('test-img.jpg')[0]
            main_type, sub_type = content_type.split('/', 1)
            msg = f.read()
            assignment.document_ref.put_attachment(name, content_type, msg)


    def get_data(self, assignment):
        for row in self.database.all_docs()['rows']:
            if row['id'] == assignment._id:
                return row
        return None



# Returns a list of attachment names
def get_attachment_names(document):
    db_attachments = document['_attachments']
    return list(map(lambda x: x, db_attachments))

# Writes attachment to disk
def write_attachment(document, attachment_name, filename):
    with open(filename, "wb") as f:
        document.get_attachment(attachment_name, write_to=f)


db = Database(API_KEY["username"], API_KEY["apikey"])

asn1 = Assignment("Assignment001", "History", "Learn about the civil war", "15/07/20")
db.create_assignment(asn1)
a = db.get_assignments()
db.add_attachment(a[0], "./test-img.jpg", "image2.jpg")

attachments = get_attachment_names(a[0].document_ref)
print(attachments)
write_attachment(a[0].document_ref, attachments[0], "img.jpg")

db.disconnect()
