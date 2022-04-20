<template>
  <div style="padding: 2rem 3rem; margin-top: 2%"> 
    <b-button v-b-modal.modal-prevent-closing>
        <b-icon icon="plus" font-scale="1"  ></b-icon>        
    </b-button>

    <label class="label">Agregar articulo:</label>

    <div class="mt-3">
      List of articles:
      <b-table striped hover :items="submittedNames" :fields="fields">
        <template #cell(load_check)="load">
          <span v-if="load.item.load_check == true">✔</span>
            <span v-else>✖</span>          
        </template>
        <template #cell(unload_check)="unload">
          <span v-if="unload.item.unload_check == true">✔</span>
            <span v-else>✖</span>          
        </template>
        
        <template #cell(description_unload)="desc_load"> 
          <span>
            <b-form-input v-model="desc_load.item.description_unload" @change="info(desc_load.item.item_number, desc_load.item.description_unload)" type="text" debounce="500"></b-form-input>    
          </span>
        </template>
        
        </b-table> 

    </div>

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Submit Your Name"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Name"
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
    
    <label class="myFile">    
        <b-icon icon="images" class="border rounded p-1" font-scale="3"  ></b-icon>
        <b-form-file class= "file" multiple :file-name-formatter="formatNames" @change="onFileSelected" lang="es"  style="display: none;" > </b-form-file>    
        <label class="custom-file-label" for="customFileLang">Por favor Seleccionar imagenes</label>
      </label> 
  </div>
</template>

<script>
import { StreamBarcodeReader } from "vue-barcode-reader";
import axios from "axios";

  export default {
    props: ['clickedNext', 'currentStep'],
    components: {
    StreamBarcodeReader,
  },
    data() {
      return {
        nameState: null,  
        barcode: '',
        submittedNames: [],
        fields: ['item_number', 'packing_reference', 'articles', 'condition_at_origin', 'exceptions_at_destination', 'load_check', 'description_load', 'unload_check', 'description_unload'],
        id_inventory : ''
        
      }
    },
    methods: {

      onFileSelected(event){        
        var token_drop = localStorage.getItem("token_drop");            
        console.log("Get value !!!!!!!!!!!!!!!");
        console.log(token_drop);

        var Dropbox = require('dropbox').Dropbox;
        var dbx = new Dropbox({ accessToken: token_drop.replace(/['"]+/g, '')});
        this.inventory_table = JSON.parse(localStorage.getItem("inventory_table") || '[]')
        axios.post("https://api.dropboxapi.com/2/files/create_folder_v2", {"path": "/" + this.inventory_table['reference'] + "/Descargue","autorename": false}, {
                headers: {
                    'Authorization': `Bearer ${token_drop.replace(/['"]+/g, '')}` 
                    }
          })

        this.selectedFile = event.target.files;

        Array.from(this.selectedFile).forEach(File => { 
          dbx.filesUpload({path: '/'+this.inventory_table['reference'] +'/Descargue/' + File.name, contents: File})
            .then(function(response) {
              console.log(response);
            })
            .catch(function(error) {
              console.error(error);
            });      
          });
      },

      info(item, description ) {   
        this.submittedNames.forEach(function (row) {
        if (row.item_number == item){
          row.description_unload = description;                    
          }           
        });
        localStorage.setItem('inventory_load_unload',JSON.stringify(this.submittedNames));
      },

      checkFormValidity() {
        const valid = this.$refs.form.checkValidity()
        this.nameState = valid
        return valid
      },
      resetModal() {
        this.nameState= null  
        this.barcode= ''
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
            
        if (this.submittedNames.length > 0 ) {
          console.log("Ok");
          this.$emit('can-continue', {value: true});
          
        }
        
        // Hide the modal manually
        this.$nextTick(() => {
          console.log("Ok");
          this.$bvModal.hide('modal-prevent-closing')
        })
      },
    onDecode (result) {
      this.barcode = result;
      this.submittedNames.forEach(function (item) {
        if (item.barcode_id == result){
          item.unload_check = true;
        }   
      });
      this.$bvModal.hide('modal-prevent-closing')
      this.$emit('can-continue', {value: true}); 
      localStorage.setItem('inventory_load_unload',JSON.stringify(this.submittedNames));
      return this.submittedNames      
      }
    },
    created() {
      const ref = 'https://www.dropbox.com/oauth2/authorize?response_type=code&client_id='+ process.env.VUE_APP_DROPBOX +'&redirect_uri=http://https://container-grouplii-frontend-uymd3d36pa-uc.a.run.app/auth&token_access_type=offline'
      window.open(ref, "_blank");
      this.id_inventory = JSON.parse(localStorage.getItem("inventory_reference") || '[]');
      axios.get("https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/get_inventory_detail/"+ this.id_inventory[0]).then((response) => {
                this.submittedNames = response.data;
                });      
    }
  }
</script>

<style scoped>


.button_add{
    background-color: rgb(255, 255, 255);
}

</style>