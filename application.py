from flask import Flask, jsonify, request

creacionapi = Flask(__name__)

from Vehiculos import vehiculos

@creacionapi.route('/ping')
def ping():
    return jsonify({"mensage":"Bienvenido!!!"})

@creacionapi.route("/Vehiculos")
def getVehiculos():
    return jsonify({"vehiculos":vehiculos, "mensaje":"Lista de Vehiculos"})

@creacionapi.route('/Vehiculos/<string:Vehiculos_nombre>')
def getVehiculo(Vehiculos_nombre):
    VehiculosFound = [vehiculos for vehiculos in vehiculos if vehiculos ['nombre'] == Vehiculos_nombre]
    if (len(VehiculosFound)> 0):
        return jsonify({"vehiculos":VehiculosFound[0]})#Solo queremos el valor 0
    return jsonify({"mensaje":"Vehucilo no encontrado"})
#AGREGAR UN VEHICULO NUEVO
@creacionapi.route('/Vehiculos', methods=['POST'])
def agregar_vehiculos():
    Nuevo_Vehiculo = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    vehiculos.append(Nuevo_Vehiculo)
    return jsonify({"mensaje":"Vehiculo se a agregado a la lista", "Vehiculos":vehiculos})

#ACTUALIZAR VEHICULOS
@creacionapi.route('/Vehiculos/<string:Vehiculos_nombre>', methods=['PUT'])
def Editar_Producto(Vehiculos_nombre):
    VehiculosFound = [vehiculos for vehiculos in vehiculos if vehiculos['nombre'] == Vehiculos_nombre]
    if (len(VehiculosFound) > 0):
        VehiculosFound[0]['nombre'] = request.json['nombre']
        VehiculosFound[0]['precio'] = request.json['precio']
        VehiculosFound[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "mensaje":"Vehiculo Actualizado", "Vehiculo": VehiculosFound[0]})
    return jsonify({"mensaje":"No se a encontrado ningun Vehiculo"})
#ELIMINAR VEHICULOS
@creacionapi.route('/Vehiculos/<string:Vehiculos_nombre>', methods=['DELETE'])
def Eliminar_Vehiculos(Vehiculos_nombre):
    VehiculosFound = [vehiculos for vehiculos in vehiculos if vehiculos['nombre'] == Vehiculos_nombre]
    if len(VehiculosFound) > 0:
        vehiculos.remove(VehiculosFound[0])
        return jsonify({
            "mensaje":"Vehiculo Eliminado de la Lista", 
            "vehiculos": vehiculos
        })
    return jsonify({"mensaje":"Vehiculo no encontrado para eliminar"})

if __name__ == '__main__':
    creacionapi.run(debug=True,port=4000)