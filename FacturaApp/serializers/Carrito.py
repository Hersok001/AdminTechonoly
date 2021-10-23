from InventariosApp.models.Inventario import inventario


class Carro:
    
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro

    def agregar(self, inventario):
        if(str(inventario.id) not in self.carro.keys()):
            self.carro[inventario.id]={
                "inventario_id":inventario.id,
                "producto":inventario.nombre_producto,
                "precio":str(inventario.precio),
                "cantidad":1,                
            }

        else:
            for key,value in self.carro.items():
                if key==str(inventario.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=int(value["precio"])+inventario.precio
                    break
        self.guardar_carro()
    #
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    #
    def eliminar(self, inventario):
        inventario.id=str(inventario.id)
        if inventario.id in self.carro:
            del self.carro[inventario.id]
            self.guardar_carro()
    #
    def restar_inventario(self, inventario):
        for key, value in self.carro.items():
            if key==str(inventario.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-inventario.precio
                if value["cantidad"]<1:
                    self.eliminar(inventario)
                    break
        self.guardar_carro()
    #
    def limpiar(self):
        self.session["carro"]={}
        self.session.modified=True
