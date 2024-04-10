from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Configuración de la base de datos MongoDB
client = MongoClient("mongodb://52.200.139.211:27017/")
db = client["Bas_datos_tareas"]
collection = db["tareas_alumnos"]

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = list(collection.find())
    # Convertir ObjectId a cadena en cada tarea
    for tarea in tareas:
        tarea['_id'] = str(tarea['_id'])
    return jsonify({"tareas": tareas})

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    data = request.json
    rut = data.pop('rut')
    tarea_id = collection.insert_one({"rut": rut, **data}).inserted_id
    return jsonify({"mensaje": "Tarea agregada exitosamente", "tarea_id": str(tarea_id)})


@app.route('/tareas/<tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    data = request.json
    collection.update_one({"_id": ObjectId(tarea_id)}, {"$set": data})
    return jsonify({"mensaje": "Tarea actualizada exitosamente"})

@app.route('/tareas/<tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    collection.delete_one({"_id": ObjectId(tarea_id)})
    return jsonify({"mensaje": "Tarea eliminada exitosamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
