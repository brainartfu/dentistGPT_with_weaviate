import weaviate
import json

# Set up the client for the local Weaviate instance

client = weaviate.Client(
    url="http://localhost:8000",
)

print('connected client')
# # empty schema and create new schema
client.schema.delete_all()
print('deleted all class')

schema = {
  "classes": [
    {
      "class": "DentalCondition",
      "description": "A dental condition or disease, such as a cavity or gum disease.",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the dental condition or disease.",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The description of the dental condition.",
          "name": "description"
        },
        {
          "dataType": ["text[]"],
          "description": "The symptoms of the dental condition or disease.",
          "name": "symptoms"
        },
        {
          "dataType": ["text[]"],
          "description": "The treatments for the dental condition or disease.",
          "name": "treatments"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    },
    {
      "class": "DentalEquipment",
      "description": "Dental equipment used by dentists, such as dental chairs or drills.",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the dental equipment.",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The description of the dental equipment.",
          "name": "description"
        },
        {
          "dataType": ["number"],
          "description": "The cost of the dental equipment.",
          "name": "cost"
        },
        {
          "dataType": ["string"],
          "description": "The dental procedure associated with the dental equipment.",
          "name": "procedure"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    },
    {
      "class": "DentalMaterial",
      "description": "Dental materials used by dentists, such as dental cement or composite resin.",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the dental material.",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The description of the dental material.",
          "name": "description"
        },
        {
          "dataType": ["number"],
          "description": "The cost of the dental material.",
          "name": "cost"
        },
        {
          "dataType": ["string"],
          "description": "The dental procedure associated with the dental material.",
          "name": "procedure"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    },
    {
      "class": "DentalProcedure",
      "description": "A dental procedure performed by a dentist, such as fillings, teeth cleaning, or root canal.",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the dental procedure.",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The description of the dental procedure.",
          "name": "description"
        },
        {
          "dataType": ["DentalEquipment"],
          "description": "The dental equipment used during the procedure.",
          "name": "equipment"
        },
        {
          "dataType": ["DentalMaterial"],
          "description": "The dental materials used during the procedure.",
          "name": "materials"
        },
        {
          "dataType": ["DentalCondition"],
          "description": "The dental condition or disease that the procedure addresses.",
          "name": "condition"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    },
    {
      "class": "DentalSchool",
      "description": "Represents dental schools and colleges that offer dental education programs",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the school or college",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The description of the dental school.",
          "name": "description"
        },
        {
          "dataType": ["text"],
          "description": "The location of the school or college",
          "name": "location"
        },
        {
          "dataType": ["text[]"],
          "description": "A list of dental education programs offered by the school or college",
          "name": "offers"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    },    
    {
      "class": "Dentist",
      "description": "A dentist who provides dental services.",
      "properties": [
        {
          "dataType": ["text"],
          "description": "The name of the dentist.",
          "name": "name"
        },
        {
          "dataType": ["text"],
          "description": "The area of specialization of the dentist.",
          "name": "specialization"
        },
        {
          "dataType": ["DentalSchool"],
          "description": "The dental school where the dentist received their training.",
          "name": "school"
        },
        {
          "dataType": ["text"],
          "description": "The dental insurance plans accepted by the dentist.",
          "name": "insurance"
        },
        {
          "dataType": ["DentalEquipment"],
          "description": "The dental equipment used during the procedure.",
          "name": "equipment"
        },
        {
          "dataType": ["DentalMaterial"],
          "description": "The dental materials used during the procedure.",
          "name": "materials"
        }
      ],
      "vectorizer": "text2vec-contextionary"
    }
  ]
}
client.schema.create(schema)
print('created all class')

# Load the data for each class from the corresponding JSON file
with open("dental_conditions.json", "r") as f:
    dental_conditions = json.load(f)

with open("school.json", "r") as f:
    dental_school = json.load(f)

with open("dental_equipment.json", "r") as f:
    dental_equipment = json.load(f)

with open("dental_materials.json", "r") as f:
    dental_materials = json.load(f)

with open("dental_procedures.json", "r") as f:
    dental_procedures = json.load(f)

with open("dentists.json", "r") as f:
    dentists = json.load(f)

print('loaded all json file')

for obj in dental_conditions:
    client.data_object.create(
        {"name": obj["name"], "description": obj["description"], "symptoms": obj["symptoms"], "treatments": obj["treatments"]},
        "DentalCondition"
    )

print('updated DentalCondition class')

for obj in dental_school:
    client.data_object.create(
        {"name": obj["name"], "location": obj["location"], "offers": obj["offers"]},
        "DentalSchool"
    )

print('updated DentalSchool class')

for obj in dental_equipment:
    client.data_object.create(
        {"name": obj["name"], "description": obj["description"],  "cost": obj["cost"], "procedure": obj["procedure"]},
        "DentalEquipment"
    )
    
print('updated DentalEquipment class')

for obj in dental_materials:
    client.data_object.create(
        {"name": obj["name"], "description": obj["description"],  "cost": obj["cost"], "procedure": obj["procedure"]},
        "DentalMaterial"
    )

print('updated DentalMaterial class')

data = {}
data['DentalMaterial'] = client.data_object.get(class_name='DentalMaterial')
data['DentalCondition'] = client.data_object.get(class_name='DentalCondition')
data['DentalEquipment'] = client.data_object.get(class_name='DentalEquipment')
data['DentalSchool'] = client.data_object.get(class_name='DentalSchool')
def get_reference(client, class_name, object_id):
    try:
        if isinstance(object_id, list):
            references = []
            for id in object_id:
                objects = data[class_name]['objects']
                for obj in objects:
                    if obj['properties']['name'] == id:
                        references.append(obj['id'])
                        break
            return references
        else:
            objects = data[class_name]['objects']
            for obj in objects:
                if obj['properties']['name'] == object_id:
                    return [obj['id']]
            return []
    except:
        return []

for obj in dental_procedures:
    equipment_reference = get_reference(client, "DentalEquipment", obj["equipment"])
    materials_reference = get_reference(client, "DentalMaterial", obj["materials"])
    condition_reference = get_reference(client, "DentalCondition", obj["condition"])
    id = client.data_object.create(
        {"name": obj["name"], "description": obj["description"]},
        "DentalProcedure"
    )
    for nid in equipment_reference:
        client.data_object.reference.add(
            from_class_name="DentalProcedure",
            from_uuid=id,
            from_property_name="equipment",
            to_class_name="DentalEquipment",
            to_uuid=nid,
        )


    for nid in materials_reference:
        client.data_object.reference.add(
            from_class_name="DentalProcedure",
            from_uuid=id,
            from_property_name="materials",
            to_class_name="DentalMaterial",
            to_uuid=nid,
        )   
    for nid in condition_reference:
        client.data_object.reference.add(
            from_class_name="DentalProcedure",
            from_uuid=id,
            from_property_name="condition",
            to_class_name="DentalCondition",
            to_uuid=nid,
        )

print('updated DentalProcedure class')

for obj in dentists:
    equipment_reference = get_reference(client, "DentalEquipment", obj["equipment"])
    materials_reference = get_reference(client, "DentalMaterial", obj["materials"])
    reference = get_reference(client, "DentalSchool", obj["school"])
    id = client.data_object.create(
        {"name": obj["name"], "specialization": obj["specialization"], "insurance": obj["insurance"]},
        "Dentist"
    )

    for nid in reference:
        client.data_object.reference.add(
            from_class_name="Dentist",
            from_uuid=id,
            from_property_name="school",
            to_class_name="DentalSchool",
            to_uuid=nid,
        )
    for nid in equipment_reference:
        client.data_object.reference.add(
            from_class_name="Dentist",
            from_uuid=id,
            from_property_name="equipment",
            to_class_name="DentalEquipment",
            to_uuid=nid,
        )
    for nid in materials_reference:
        client.data_object.reference.add(
            from_class_name="Dentist",
            from_uuid=id,
            from_property_name="materials",
            to_class_name="DentalMaterial",
            to_uuid=nid,
        )

print('updated Dentist class')
