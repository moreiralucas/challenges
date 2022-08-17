<template>
  <div class="home">  
    <h1>Notificações</h1>
    <div class="contentContainer">
      <div v-for="element in notifications" :key="element.id">
        {{ element.id }} - {{ element.text }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import services from "@/services/";
import { Component, Vue } from "vue-property-decorator";
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
// import { Manager, io, Socket} from 'socket.io-client';
// import VueSocketIo from 'vue-socket.io';


@Component({
  components: { HelloWorld },
})
export default class Home extends Vue {
  isLoading = false;
  isFailed = false;
  failMessage = "";

  notifications = [{
    id: 1,
    text: "Lucas"
  }];

  async mounted(): Promise<void> {
    await this.getNotificationsData();
    // this.connect();
  }

  async created(): Promise<void> {
    this.connect();
  }

  connect(){
    console.log('Method in HomeView');

    this.$socket.on('connection', (data) => {
      console.log("Conected:", data);
    });


    this.$socket.on('occurrence', (data) => {
      console.log("data:", data);
      console.log("message:", data.message);
    });

    this.$socket.on('listener', (data) => {
      console.log("data:", data);
      console.log("message:", data.message);
    });

    this.$socket.emit('pingServer', 'PING!');
  }

  async getNotificationsData(
    page = 1,
    page_size = 50,
    order: string[] = []
  ): Promise<void> {
    this.isLoading = true;

    try {
      const response = await services.api.v1.getNotifications(
        page,
        page_size,
        order.toString(),
        this.test_filter,
        this.status_filter,
        this.search,
      );

      this.notifications = response.data;

      this.isFailed = false;
      this.failMessage = "";
    } catch (error) {
      this.isFailed = true;
    } finally {
      this.isLoading = false;
    }
  }
  
}
</script>

<style lang="scss" scoped></style>
