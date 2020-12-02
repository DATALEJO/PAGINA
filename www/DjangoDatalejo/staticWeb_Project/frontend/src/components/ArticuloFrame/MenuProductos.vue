<template >
  <section >
    <div class="container-fluid" :style= "{ backgroundImage: 'url(' + require('@/assets/fondoTodo.png') + ')' }">
        <h1 class="titleArticle" style="text-align:center; " >NUESTROS PRODUCTOS</h1>
        <div class="row"  >
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/DroneFacade" >
                    <img :src="require('@/assets/' + imagenFondo0 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% 0% 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" ><br>{{tituloArticulo0}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo0}}</p>
                </router-link>
            </div>
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/CadDrone" >
                    <img :src="require('@/assets/' + imagenFondo1 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% 0% 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" ><br>{{tituloArticulo1}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo1}}</p>
                </router-link>
            </div>
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/InventEye" >
                    <img :src="require('@/assets/' + imagenFondo2 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% 0% 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" ><br>{{tituloArticulo2}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo2}}</p>
                </router-link>
            </div>
          </div>
          <div class="row"  >
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/" >
                    <img :src="require('@/assets/' + imagenFondo3 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% % 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" ><br>{{tituloArticulo3}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo3}}</p>
                </router-link>
            </div>
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/Sencore" >
                    <img :src="require('@/assets/' + imagenFondo4 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% 0% 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" ><br>{{tituloArticulo4}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo4}}</p>
                </router-link>
            </div>
            <div class="col-md-4" style="padding:4%;">
                <router-link  to="/" >
                    <img :src="require('@/assets/' + imagenFondo5 + '')"  
                        style="border-radius:10px 10px 10px 10px; width: 100%;margin: 0% 0% 0% 0%;"> 
                    <h2 class="titleArticle" style="text-align:center;" >{{tituloArticulo5}}</h2>
                    <p class="textArticle" style="text-align:justify; text-justify:inter-character; " ><br>{{textoArticulo5}}</p>
                </router-link>
            </div>
          </div>
    </div>
  </section>
</template>

<script>
import Parallax from "vue-parallaxy";
//import { PlyrVideo } from 'vue-plyr';

export default {
  name: 'articuloFrame',
  components: {   
       Parallax,
  //      PlyrVideo
  },
  props: {
      tituloArticulo0:{
        type: String,
        default:"Análisis de Fachadas"
      },
      textoArticulo0:{
        type: String,
        default:"Usamos drones para hacer el análisis de fachadas"
      },
      imagenFondo0:{
        type: String,
        default:"drone_Facade1.png"
      },
      tituloArticulo1:{
        type: String,
        default:"Modelos 2D y 3D para estructura"
      },
      textoArticulo1:{
        type: String,
        default:"Capturamos y procesamos los datos que permitén generar los modelos 3D "
      },
      imagenFondo1:{
        type: String,
        default:"cap_dron10.png"
      },
      tituloArticulo2:{
        type: String,
        default:"Inspección de maquinaría"
      },
      textoArticulo2:{
        type: String,
        default:"Usamos imagenes para revisar maquinaría"
      },
      imagenFondo2:{
        type: String,
        default:"inspeccion_Maquinaria0.png"
      },
      tituloArticulo3:{
        type: String,
        default:"Avance de obra"
      },
      textoArticulo3:{
        type: String,
        default:"Hacemos análisis multitemporal de su proyecto"
      },
      imagenFondo3:{
        type: String,
        default:"avance_Obra0.png"
      },
      tituloArticulo4:{
        type: String,
        default:"Sensores a la medida"
      },
      textoArticulo4:{
        type: String,
        default:"Desarrollo de hardware que permite capturar y analizar información"
      },
      imagenFondo4:{
        type: String,
        default:"sen_core5.png"
      },
      tituloArticulo5:{
        type: String,
        default:"Machine Learning"
      },
      textoArticulo5:{
        type: String,
        default:"Procesamos los datos capturados para encontrar información adicional de la estructura"
      },
      imagenFondo5:{
        type: String,
        default:"machine_Learning0.png"
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
.titleArticle{

  color: rgb(63,69,77);
  /*font-size: 24px;*/
  font-size: 2.2vw;
  text-align:justify;
}
/*
.row .col-md-4{
  z-index: 1;
}*/
.textArticle{
  /*font-size: medium;*/
  color: rgb(109,113,120);
  /*font-size: 16px;*/
  font-size: 1.3vw;
  white-space: pre-wrap;
  text-align:justify;

}

@media only screen and (max-width: 800px) { 

 .textArticle{
  text-align:justify;
    font-size: 5vw;
    /*font-size: 24px;*/
}
.titleArticle{
  text-align:justify;
    font-size: 6vw;
    /*font-size: 16px*/
  }
}


.container-fluid{
  position: relative;
  /*height: 500px;*/
  /*width: 100%;*/
  padding: 0vh;
  /*z-index: -1;*/
  background-image: '@/assets/fondoTodo.png';
  padding: 4% 0% 4% 0%;
}
.contenedor-paralax{
  position: relative;
  /*z-index: -1;*/
}

.frameBack1{
  position: relative;
  /*background-color: #05668d;*/
  /*z-index: -2;*/
}
.frameBack{
  position: relative;
    /*background-color: #05668d;
    color: #028090;*/
    /*background-color: #1b222c;/*
    color: #8d99ae;
    color: #edf2f4; */
    /*color: #02c39a;*/
  /*speed-factor:"0.5";*/
  /*direction:'down';*/
  /*sectionHeight: "170";*/
  top: 0;
  left: 0;
  /*width: 100%;*/
  /*height:100vh;*/
  /*z-index: -1;*/
}
.video{
  width: 100%;
  /*height:100vh;*/
  border-radius:10px 10px 10px 10px;
  margin: 15% 0% 0% 0%;
}

.frameFront{
  position: absolute;
  /*direction:'up';*/
  top: 0;
  left: 0;
  width: 100%;
  /*height:100%;*/
  /*z-index: 0;*/
  /*height:"1600";*/

}

.parallax-title {
  position: absolute;
  top: 50vh;
  left: 0;
  right: 0;
  padding: 20px;
  background: rgba(0, 0, 0, 0.315);
  color: rgb(200, 205, 221);
  text-align: center;
}

/*
@media screen and (max-width: 600px){
  .container-fluid{
    height: 150vh;
  }
}
*/
.pre{
  border: transparent;
  background-color: transparent;
}
</style>