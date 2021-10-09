class Intervalle:
    def __init__(self,a,b): #l'intervalle [a,b]
            self.borne_inf = a
            self.borne_sup = b
            return None


    def val_inf(self,val1,val2):
        if val1 <= val2:
            return val1
        return val2

    
    def val_sup(self,val1,val2):
        if val1 >= val2:
            return val1
        return val2
 
    
    def __contains__(self,val): #renvoie True si val est dans l'intervalle
        return val >= self.borne_inf and val <= self.borne_sup

    
    def __eq__(self,intervalle): # test égalité avec un autre intervalle
        return intervalle._get_borne_inf() == self.borne_inf and intervalle._get_borne_sup() == self.borne_sup

    
    def __le__(self,intervalle): #renvoie True si l'intervalle est inclu dans un autre intervalle
        return self.borne_inf >= intervalle._get_borne_inf() and intervalle._get_borne_sup() >= self.borne_sup

    
    def __intersection__(self,intervalle): #renvoie l'intersection de deux intervalles              
        borne_inf,borne_sup = self.val_sup(intervalle._get_borne_inf(),self.borne_inf),self.val_inf(intervalle._get_borne_sup(),self.borne_sup)            
        if borne_inf > borne_sup:
            return None         
        return [borne_inf,borne_sup]

    
    def __union__(self,intervalle): #renvoie le plus petit intervalle qui contient les deux intervalles                
        borne_inf,borne_sup = self.val_inf(intervalle._get_borne_inf(),self.borne_inf),self.val_sup(intervalle._get_borne_sup(),self.borne_sup)          
        return [borne_inf,borne_sup]
    
    
    def __str__(self):
        return str([self.borne_inf,self.borne_sup])
    
    
    def __repr__(self):
        return self.__str__()
    
    
    def est_vide(self):
        return self.borne_inf > self.borne_sup
    
    
    def _get_borne_inf(self):
        return self.borne_inf
    
    
    def _get_borne_sup(self):
        return self.borne_sup