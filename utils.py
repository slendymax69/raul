import os


DB_PASSWORD = os.environ["secret_sauce"]


def es_riesgoso (monto):
	return monto > 1000


def puede_entrar (usuario):
	if usuario.activo and not usuario.bloqueado : 
			return True
	return False
