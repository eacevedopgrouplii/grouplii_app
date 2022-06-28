<template>
  <div class="add-barcode">        
    <b-button v-b-modal.modal-prevent-closing>
        <img src="https://www.pngall.com/wp-content/uploads/10/Plus-Symbol-PNG-Pic.png" width="20" />
    </b-button>

    <label class="label">Ingrese articulo evaluar proceso:</label>

    <div v-if="cargue" class="d-flex justify-content-center" style="margin-top: 5%">     
      <b-card
      :header=" 'Proceso: '  + status_inventory"
      header-tag="header"
      :footer="'Cliente: ' + clients_name"
      footer-tag="footer" 
      :title="'Inventario: '+ inventory_reference"
      style="max-width: 20rem;"
    >
      <b-card-text>Artículo evaluado : {{barcode}} </b-card-text>
      <b-button :href="link_continue" variant="primary">Continuar</b-button>
    </b-card>

    </div>  
   
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Seguimiento Inventario"
      @show="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Artículo para seguimiento"
          label-for="name-input"
        >         

          Input Value: {{ barcode || "Nothing" }}
          <StreamBarcodeReader
                @decode="onDecode"
                @loaded="onLoaded"
            ></StreamBarcodeReader>

        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from "axios";

  export default {
    components: {
    StreamBarcodeReader,
  },
    data() {
      return {
        nameState: null,
        barcode: '',
        cargue: false,
        link_continue: '',
        inventory_detail : [],     
        inventory_reference : '',
        clients_name: '',
        status_inventory: '',
        clients_email: ''  
      }
    },
    methods: {
      checkFormValidity() {
        const valid = this.$refs.form.checkValidity()
        this.nameState = valid
        return valid
      },
      resetModal() {
        this.nameState= null,
        this.barcode = '',
        this.cargue = false
      },
      handleOk(bvModalEvt) {
        // Prevent modal from closing
        bvModalEvt.preventDefault()
        // Trigger submit handler
        this.handleSubmit()
      },
      handleSubmit() {
        // Exit when the form isn't valid
        if (!this.checkFormValidity()) {
          return
        }                       
        
        // Hide the modal manually
        this.$nextTick(() => {
          this.$bvModal.hide('modal-prevent-closing')
        })
      },
    onDecode (result) {
        this.barcode = result;
        this.$bvModal.hide('modal-prevent-closing')

        axios.get("https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/get_inventory/"+ result).then((response) => {

                this.inventory_detail = response.data;
                this.inventory_reference = this.inventory_detail[0]['inventory_reference'];
                this.clients_name = this.inventory_detail[0]['clients_name'];
                this.clients_email = this.inventory_detail[0]['inventory_email'];
                localStorage.setItem('inventory_reference',JSON.stringify([this.inventory_reference, this.clients_name, this.clients_email]));
                console.log(this.inventory_detail['status_inventory'])
                if (this.inventory_detail[0]['status_inventory'] == "packing"){   
                  this.status_inventory = "cargue"               
                  this.cargue = true;
                  this.link_continue = 'load_inventory'
                } else if (this.inventory_detail[0]['status_inventory'] == "load"){
                  this.status_inventory = "descargue"
                  this.cargue = true;
                  this.link_continue = 'unload_inventory'
                } else {
                  alert("Ya FInalizamos")
                }
                

              });        
  }
    }
  }
</script>

<style scoped>

.add-barcode{
  
    position: absolute;
    left: 32%;  
    top: 30%;  
    width: 40%;
    height: 25% ;
  
}

.button_add{
    background-color: rgb(255, 255, 255);
}

</style>