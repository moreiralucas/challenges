import Vuex from "vuex";

import { GlobalStore } from "./GlobalStore";

// Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isConnected: false,
    socketMessage: ''
  },
  mutations: {
    SOCKET_CONNECT(state) {
      state.isConnected = true;
    },

    SOCKET_DISCONNECT(state) {
      state.isConnected = false;
    },

    SOCKET_OCCURRENCE(state, message) {
      state.socketMessage = message
    },
  },
  actions: {
    "occurrence"(){
      console.log('occurrence test');
    }
  },
  modules: {
      GlobalStore,
  },
});
