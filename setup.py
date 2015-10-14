from distutils.core import setup  
  
setup(name="dbConnection",  
      version="0.1",  
      description="Ejemplo de aplicacion para conectarse a MySQL, Oracle, MongoDB y POstgreSQL",  
      author="Tedezed",  
      author_email="zerrotchanel@gmail.com",  
      url="",  
      license="GPL",  
      install_requires=[
                        "PyQt4",
                        "mysqldb",
                        "psycopg2",
                        "cx_Oracle",
                        "pymongo==2.7.2"
                        ]  
)  
