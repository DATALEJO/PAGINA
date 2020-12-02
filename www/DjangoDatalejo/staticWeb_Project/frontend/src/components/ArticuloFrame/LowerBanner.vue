<template >
    <section class="contbanner" >
        <div class="container-fluid" >
            <div class="row "  >
                <div class="col-12" >
                    <div class="row "  >
                        <div class="col-3" >
                            <h1 class="titleArticle" ><br><br><br>DATALEJO.COM</h1>
                            <!--<h2 class="textArticle" align="justifed" >{{textoSubArticuloC}}<br></h2>-->
                        </div>
                        <div class="col-3" >
                            <h1 class="titleArticle"><br><br><br>{{tituloSubArticuloC}}</h1>
                            <!--<h2 class="textArticle" align="justifed" >{{textoSubArticuloC}}<br></h2>-->
                            <router-link class="frame-classic" to="/Contactenos">
                                <h2 class="textArticle" align="justifed" >{{textoSubArticuloCA}}<br></h2>
                            </router-link>
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloCB}}<br></h2>
                                <router-link class="frame-classic" to="/Contacto">
                                    <h2 class="textArticle" align="justifed" >{{textoSubArticuloCC}}<br><br></h2>
                                </router-link>
                        </div>
                        <div class="col-3" >
                            <h1 class="titleArticle"><br><br><br>{{tituloSubArticuloA}}</h1>
                            <!--<h2 class="textArticle" align="justifed" >{{textoSubArticuloA}}<br></h2>-->
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloAA}}<br></h2>
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloAB}}<br></h2>
                            <router-link class="frame-classic" to="/terminosServicio">
                                <h2 class="textArticle" align="justifed" >{{textoSubArticuloAC}}<br></h2>
                            </router-link>                        
                        </div>
                        <div class="col-3" >
                            <h1 class="titleArticle"><br><br><br>{{tituloSubArticuloB}}</h1>
                            <!--<h2 class="textArticle" align="justifed" >{{textoSubArticuloB}}<br></h2>-->
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloBA}}<br></h2>
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloBB}}<br></h2>
                            <h2 class="textArticle" align="justifed" >{{textoSubArticuloBC}}<br></h2>
                        </div>
                    </div>
                    <div class="row "  >
                        <div class="col-8" >
                            <h1 class="titleArticle" style="font-size: 0.9em;"><br>{{textoSubArticuloDA}}</h1>      
                            <h1 class="titleArticle" style="font-size: 0.9em;">{{tituloSubArticuloD}}</h1>               
                        </div>
                        <div class="col-1" style="padding:0; margin:0;"><br>
                            <img  :src="require('@/assets/' + imagenConGamma + '')" alt="front"   
                            style="height: 30%; width: 30%; object-fit: contain">
                        </div>      
                        <div class="col-1" style="padding:0; margin:0;"><br>
                            <img  :src="require('@/assets/' + imagenConGamma1 + '')" alt="front"   
                            style="height: 30%; width: 30%; object-fit: contain">
                        </div>
                        <div class="col-1" style="padding:0; margin:0;"><br>
                            <a href="https://www.instagram.com/contactodatalejo/">
                              <img  :src="require('@/assets/' + imagenConGamma2 + '')" alt="front"   
                              style="height: 30%; width: 30%; object-fit: contain">
                            </a>
                        </div>
                        <div class="col-1" style="padding:0; margin:0;"><br>
                            <a href="https://business.facebook.com/Datalejo/?business_id=1185923698472797">
                              <img  :src="require('@/assets/' + imagenConGamma3 + '')" alt="front"  
                              style="height: 30%; width: 30%; object-fit: contain"> 
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  </section>
</template>

<script>
export default {
  name: 'articuloFrame',
  props: {
      imagenConGamma:{
        type: String,
        default:"banner1.png"
      },
      imagenConGamma1:{
        type: String,
        default:"banner2.png"
      },
      imagenConGamma2:{
        type: String,
        default:"banner3.png"
      },
      imagenConGamma3:{
        type: String,
        default:"banner4.png"
      },
      tituloSubArticuloA:{
        type: String,
        default:"LEGAL"
      },
      textoSubArticuloAA:{
        type: String,
        default:"Politica Seguridad y Cookies"
      },
      textoSubArticuloAB:{
        type: String,
        default:"Politica de protección de Datos "
      },
      textoSubArticuloAC:{
        type: String,
        default:"Terminos y Condiciones"
      },
      textoSubArticuloAD:{
        type: String,
        default:"hardware Iot"
      },
      tituloSubArticuloB:{
        type: String,
        default:"DOCUMENTOS"
      },
      textoSubArticuloBA:{
        type: String,
        default:"Quickstarts"
      },
      textoSubArticuloBB:{
        type: String,
        default:"Tutoriales "
      },
      textoSubArticuloBC:{
        type: String,
        default:"Referencias de API"
      },
      textoSubArticuloBD:{
        type: String,
        default:"Manuales"
      },
      tituloSubArticuloC:{
        type: String,
        default:"COMPAÑIA"
      },
      textoSubArticuloCA:{
        type: String,
        default:"Acerca de Datalejo"
      },
      textoSubArticuloCB:{
        type: String,
        default:"Proveedores"
      },
      textoSubArticuloCC:{
        type: String,
        default:"Contáctenos"
      },
      textoSubArticuloCD:{
        type: String,
        default:"Hable con nuestros expertos"
      },
      tituloSubArticuloD:{
        type: String,
        default:"LEGAL|PRIVACIDAD|PROTECCION DE DATOS|BLOG"
      },
      textoSubArticuloDA:{
        type: String,
        default:"© 2020 DATALEJO "
      },
  }
};
</script>
<style scoped>
/*@font-face {
  font-family: 'FoundryGridnik';
  // Antes de descargar el archivo, le decimos al buscador
  //que intente buscar en local la fuente con nombre
  //Cabin, Cabin Regular o Cabin-Regular 
  src: local('FoundryGridnik'),
       local('FoundryGridnik Medium'),
       local('@assets/FoundryGridnikMedium/FoundryGridnikMedium.oft'),
       url(http://fontsgeek.com/fonts/FoundryGridnik-Bold) format('otf');
}*/
.textArticle{
  font-size: 1vw;
  color: white;
}
.titleArticle{
  font-size: 1vw;
   font-weight: bold;
   color: white;
}


@media only screen and (max-width: 600px) { 
  .textArticle{
    font-size: 2.5vw;
    color: white;
  }
  .titleArticle{
    font-size: 2.5vw;
    font-weight: bold;
    color: white;
  } 
}

.container-fluid{
  position: relative;
  /*height: 500px;*/
  background-color: rgb(27,34,44);
  z-index: 1;
  /*width: 100%;*/
}

/*
.parallax-title {
  position: absolute;
  top: 50vh;
  left: 0;
  right: 0;
  padding: 20px;
  //background: rgba(0, 0, 0, 0.315);
  color: rgb(200, 205, 221);
  text-align: center;
}*/

/*.contbanner{
    height: 30vh;
}*/

</style>