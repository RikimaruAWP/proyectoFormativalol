from django.db import models

class Candidato:
    def __init__(self, nombre, apellido, votos=0):
        self.nombre = nombre
        self.apellido = apellido
        self.votos = votos

class Elecciones:
    def __init__(self):
        self.candidatos = []

    def buscarCandidato(self, nombre, apellido):
        for candidato in self.candidatos:
            if candidato.nombre == nombre and candidato.apellido == apellido:
                return candidato

    def inscribir(self, candidato):
        if not isinstance(candidato, Candidato):
            return "Error: Candidato debe ser una instancia de la clase Candidato."
        result = self.buscarCandidato(candidato.nombre, candidato.apellido)
        if result is not None:
            return "Error: Candidato ya inscrito."
        self.candidatos.append(candidato)
        return "Candidato inscrito con éxito."

    def votar(self, nombre, apellido):
        candidato = self.buscarCandidato(nombre, apellido)
        if candidato:
            candidato.votos += 1
            return "Voto registrado con éxito."
        else:
            return "Error: Candidato no encontrado."

    def resultados(self):
        if not self.candidatos:
            return "Error: No hay candidatos inscritos."
        else:
            ganador = max(self.candidatos, key=lambda x: x.votos)
            return ganador
