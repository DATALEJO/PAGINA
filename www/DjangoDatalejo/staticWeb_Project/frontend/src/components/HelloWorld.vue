<template>
    <div class="contenedor-todo">
    <paralax_dl></paralax_dl>
    <div >
      <articuloFrame  
        v-bind:tituloArticulo= "title0" 
        v-bind:textoArticulo= "article0" 
        v-bind:textoSobreImagen= "textimg0"
        v-bind:imagenConGamma= "imagenConGamma0"
        v-bind:imagenFondo= "imagenFondo0"
      />
    </div>
    <div class="frame-classic-short">
      <articuloIntermedio 
        v-bind:articuloInter= "articuloInter0"
      />
    </div>
    <div class="frame-classic">
        <articuloImaTresCols  
            v-bind:imagenConGamma= "imagenConGamma1" 
            v-bind:tituloSubArticuloA= "tituloSubArticuloA0" 
            v-bind:textoSubArticuloA= "textoSubArticuloA0"
            v-bind:textoSubArticuloB= "textoSubArticuloB0"
            v-bind:textoSubArticuloC= "textoSubArticuloC0"
            v-bind:imagenSubArticuloA= "imagenSubArticuloA0"
            v-bind:imagenSubArticuloB= "imagenSubArticuloB0"
            v-bind:imagenSubArticuloC= "imagenSubArticuloC0"
        />
    </div>
    <div class="frame-classic-long">
      <articuloIzqFrameColor 
        v-bind:tituloArticulo= "titleArt"
        v-bind:tituloSubArticulo= "title2" 
        v-bind:textoSubArticulo= "article2" 
        v-bind:tituloSubArticuloA= "title21" 
        v-bind:textoSubArticuloA= "article21"
        v-bind:tituloSubArticuloB= "title22" 
        v-bind:textoSubArticuloB= "article22" 
        v-bind:tituloSubArticuloC= "title23" 
        v-bind:textoSubArticuloC= "article23"  
        v-bind:textoSobreImagen= "textimg2"
        v-bind:imagenConGamma= "imagenConGamma2"
        v-bind:color= "imagenFondo2"
      />
    </div>
    <router-link class="frame-classic" to="/Contactenos">
      <articuloIzqFrame  
        v-bind:tituloArticulo= "title3" 
        v-bind:textoArticulo= "article3" 
        v-bind:textoSobreImagen= "textimg3"
        v-bind:imagenConGamma= "imagenConGamma3"
        v-bind:imagenFondo= "imagenFondo3"
      />
    </router-link>
    <div class="frame-classic-short">
      <articuloIntermedio 
        v-bind:articuloInter= "articuloInter1"
      />
    </div>
    <div>
      <lowerBanner />
    </div>
  </div>
</template>

<script>
import paralax_dl from '@/components/ParalaxVue/ParalaxVue.vue';
import articuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import articuloIzqFrame from '@/components/ArticuloFrame/ArticuloIzqFrame.vue';
import articuloIzqFrameColor from '@/components/ArticuloFrame/ArticuloIzqFrameColor.vue';
import lowerBanner from '@/components/ArticuloFrame/LowerBanner.vue';
import articuloIntermedio from '@/components/ArticuloIntermedio/ArticuloIntermedio.vue';
import articuloImaTresCols from '@/components/ArticuloFrame/ArticuloImaTresCols.vue';

export default {
  components: {
    paralax_dl,
    articuloFrame,
    articuloIntermedio,
    articuloImaTresCols,
    articuloIzqFrameColor,
    articuloIzqFrame,
    articuloFrame,
    lowerBanner
  },
  data(){
    return {
      title0:'Datos en la nube, Información disponible',
      article0:'Datalejo es una empresa enfocada en capturar, procesar y '+
              'analizar datos  usando como fuente sensores, tecnologías IoT “Internet Of Things” y  '+
              ' algoritmos de inteligencia artificial creando tableros de resúmenes orientados a la '+
              'toma de decisiones con soluciones asequibles en costo. La captura de datos se realiza '+
              'usando  vehículos no tripulados o desarrollando  hardware a la medida.',
      textimg0: 'Sencore',
      imagenConGamma0:"quehacemos.png",
      imagenFondo0:"ImagenQueHacemos.png",
      
      articuloInter0:'Trabajamos con pequeñas  medianas y grandes empresas asesorando de forma personalizada '+
                    'sus necesidades para llegar a una solución conjunta. Con nuestros productos y servicios '+
                    'impulsamos su transformación digital. ',
      
      tituloSubArticuloA0: '' ,
      textoSubArticuloA0: 'Sensamos para optimizar sus costos de operación.',
      textoSubArticuloB0: 'Capturamos datos y de esta forma podrá ampliar su capacidad de decisión.',
      textoSubArticuloC0: 'Generamos reportes que permiten tomar decisiones en el menor tiempo posible.',
      imagenConGamma1: "ImagenServicios1.png" ,
      imagenSubArticuloA0:"sensor.png",
      imagenSubArticuloB0:"report.png",
      imagenSubArticuloC0:"seo-report.png",

      titleArt:"BENEFICIOS",
      title2:'Mejoramos la velocidad de toma de decisiones:',
      article2:'Por medio del uso de  sensores y algoritmos procesamos y analizamos los datos para que  tome mejores decisiones en el menor tiempo posible.',
      title21:'Le ayudademos a que decida mejor',
      article21:' Al combinar tecnología IoT con algoritmos inteligencia artificial y el desarrollo de Hardware podemos adquirir nueva información con la que usted puede mejorar su capacidad de decisión.',
      title22 :'Presentación de la información:',
      article22:'Hacemos que la información obtenida sea fácilmente interpretable.',
      title23 : 'Disminuimos costos:',
      article23:' Realizamos un estudio de costos a medida  basados en su presupuesto.',
      textimg2: ' ',
      imagenConGamma2:"LogIllo.png",
      imagenFondo2:"rgb(63,69,77)",

      title3:'Nosotros',
      articuloInter1:'Estamos comprometidos en impulsar  la transformación de las organizaciones al paradigma de la industria 4.0 para promover nuevos modelos de negocio y así hacer más competitivas a las  empresas.',
      textimg3: 'CapDrone',
      imagenConGamma3:"Nosotros.png",
      imagenFondo3:"ImagenNosotros.png",

      article3:'Datalejo S.A.S. esta conformada por un grupo de ingenieros  con más de 10 años de experiencia en áreas como el uso de sensores, diseño hardware, construcción de soluciones firmware-software, análisis de datos y creación de dashboards orientados a la inteligencia de negocio.',
    }
  }


}
</script>

<style>
a:link
{
text-decoration:none;
  color: rgb(63,69,77);
}
.contenedor-frontal-navbar{
  z-index: 1;
}
.contenedor-todo{
  z-index: 0;
}


/*color subtitulos (63,69,77)
Color letra  general : (109,113,120) 16px*/

/*
.frame-classic{
    height: 95vh;
}

.frame-classic-long{
    height: 100vh;
}
.frame-classic-short{
    height: 45vh;
}*/
</style>
