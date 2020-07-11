import Vue from 'vue'
import Router from 'vue-router'
import Inicio from '@/components/HelloWorld';

import ListNavbar from '@/components/page_web/ListNavbar';
import ParalaxVue from '@/components/ParalaxVue/ParalaxVue';
import ArticuloFrame from '@/components/ArticuloFrame/ArticuloFrame.vue';
import ArticuloIntermedio from '@/components/ArticuloIntermedio/ArticuloIntermedio.vue';

import Sencore from '@/components/content/SencorePage';
import CadDrone from '@/components/content/CadDronePage';
import MapSafe from '@/components/content/MapSafePage';
import RetailHere from '@/components/content/RetailHerePage';
import DroneFacade from '@/components/content/DroneFacadePage';
import InventEye from '@/components/content/InventEyePage';
import Contactenos from '@/components/content/ContactenosPage';
import Contacto from '@/components/content/FormularioContacto';
import TerminosServicio from '@/components/content/TerminosServicioPage';


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: Inicio
    },
    {
      path: '/Sencore',
      name: 'Sencore',
      component: Sencore,
      props: true
    },
    {
      path: '/CadDrone',
      name: 'CadDrone',
      component: CadDrone
    },
    {
      path: '/MapSafe',
      name: 'MapSafe',
      component: MapSafe,
      //props: true
    },
    {
      path: '/RetailHere',
      name: 'RetailHere',
      component: RetailHere,
      //props: true
    },
    {
      path: '/DroneFacade',
      name: 'DroneFacade',
      component: DroneFacade,
      //props: true
    },
    {
      path: '/InventEye',
      name: 'InventEye',
      component: InventEye,
      //props: true
    },
    {
      path: '/Contactenos',
      name: 'Contactenos',
      component: Contactenos,
      //props: true
    },
    {
      path: '/Contacto',
      name: 'Contacto',
      component: Contacto,
      //props: true
    },
    {
      path: '/TerminosServicio',
      name: 'TerminosServicio',
      component: TerminosServicio,
      //props: true
    },
  ],
  scrollBehavior() {
      return {x: 0, y: 0}
  }
  /*mode:'history'*/
})