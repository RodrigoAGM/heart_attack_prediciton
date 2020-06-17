<template>
  <div id="app">
    <b-modal id="bv-modal-heart-attack" hide-footer>
      <template v-slot:modal-title>Heart attack prediction result</template>
      <div class="d-block text-center">
        <h3>{{result}}</h3>
        <h5>Porcentaje de precision: {{accuracy}}%</h5>
      </div>
      <b-button class="mt-3" block @click="$bvModal.hide('bv-modal-heart-attack')">Ok</b-button>
    </b-modal>
    <div class="container">
      <h1>SI404: Predicción de ataque al corazón</h1>
      <div class="row">
        <div class="col-sm">
          <b-form-group label="Genero">
            <b-form-radio-group
              id="btn-radios-gender"
              v-model="selectedSex"
              :options="optionsSex"
              buttons
              button-variant="outline-primary"
              size="lg"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-form-group>
          <b-form-group label="Resultados electrocardiográficos en reposo">
            <b-form-radio-group
              id="btn-radios-gender"
              v-model="selectedElectro"
              :options="optionsElectro"
              buttons
              button-variant="outline-primary"
              size="lg"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-form-group>
          <b-form-group label="Presión arterial en reposo (mm Hg)">
            <b-form-input v-model="trestbps" type="number"></b-form-input>
          </b-form-group>
          <b-form-group label="Suero colestoral en mg/dl">
            <b-form-input v-model="chol" type="number"></b-form-input>
          </b-form-group>
          <b-form-group label="Angina inducida por ejercicio">
            <b-form-radio-group
              id="btn-radios-gender"
              v-model="selectedExercise"
              :options="optionsExercise"
              buttons
              button-variant="outline-primary"
              size="lg"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-form-group>
        </div>
        <div class="col-sm">
          <b-form-group label="Edad">
            <b-form-input v-model="age" type="number"></b-form-input>
          </b-form-group>
          <b-form-group label="Tipo de dolor en el pecho">
            <b-form-radio-group
              id="btn-radios-gender"
              v-model="selectedChestPain"
              :options="optionsChestPainType"
              buttons
              button-variant="outline-primary"
              size="lg"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-form-group>
          <b-form-group label="Glucemia en ayunas (FBS)">
            <b-form-radio-group
              id="btn-radios-gender"
              v-model="selectedFbs"
              :options="optionsFbs"
              buttons
              button-variant="outline-primary"
              size="lg"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-form-group>
          <b-form-group label="Frecuencia cardíaca máxima alcanzada">
            <b-form-input v-model="thalach" type="number"></b-form-input>
          </b-form-group>
          <b-form-group label="Depresión del ST inducida por el ejercicio relativo al descanso">
            <b-form-input v-model="oldpeak" type="number"></b-form-input>
          </b-form-group>
        </div>
      </div>
      <b-button block pill id="predict-btn" variant="primary" @click="predictHeartAttack">PREDECIR</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      result: "NO RESULT",
      accuracy: 0,
      selectedSex: 0,
      optionsSex: [
        { text: "Femenino", value: 0 },
        { text: "Masculino", value: 1 }
      ],
      selectedFbs: 0,
      optionsFbs: [
        { text: "Verdaero", value: 1 },
        { text: "Falso", value: 0 }
      ],
      selectedElectro: 0,
      optionsElectro: [
        { text: "Normal", value: 0 },
        { text: "Anormalidad en ST-T", value: 1 },
        { text: "Hipertrofia ventricular izquierda", value: 2 }
      ],
      selectedChestPain: 1,
      optionsChestPainType: [
        { text: "Angina típica", value: 1 },
        { text: "Angina atípica", value: 2 },
        { text: "No hay dolor", value: 3 },
        { text: "Asintomático", value: 4 }
      ],
      selectedExercise: 0,
      optionsExercise: [
        { text: "Si", value: 1 },
        { text: "No", value: 0 }
      ],
      oldpeak: null,
      thalach: null,
      age: 18,
      trestbps: null,
      chol: null
    };
  },
  methods: {
    predictHeartAttack() {
      var data = {
        age: this.age,
        sex: this.optionsSex[this.selectedSex].value,
        cp: this.optionsChestPainType[this.selectedChestPain].value,
        trestbps: Number(this.trestbps),
        chol: Number(this.chol),
        fbs: this.optionsFbs[this.selectedFbs].value,
        restecg: this.optionsElectro[this.selectedElectro].value,
        thalach: Number(this.thalach),
        exang: this.optionsExercise[this.selectedExercise].value,
        oldpeak: Number(this.oldpeak)
      };
      axios({
        method: "POST",
        url: " http://localhost:5000/predict",
        data: data
      }).then(
        result => {
          console.log(result);
          this.result = result.data.response;
          this.accuracy = result.data.accuracy;
          this.$bvModal.show("bv-modal-heart-attack");
          this.results = result.data;
        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
