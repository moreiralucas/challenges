import { Module, VuexModule } from "vuex-module-decorators";

@Module({ name: "GlobalStore", namespaced: true })
export class GlobalStore extends VuexModule {
  private _environment = process.env.VUE_APP_ENVIRONMENT;

  get environment(): string {
    return this._environment;
  }

}
