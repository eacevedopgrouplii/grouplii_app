<template>
<section class="section">
    <div class="container">
        <div class="columns">
            <div class="column is-8 is-offset-2">
                <horizontal-stepper :steps="demoSteps" @completed-step="completeStep"
                                    @active-step="isStepActive" @stepper-finished="alert"
                >                     
                </horizontal-stepper>
            </div>
        </div>
    </div>
</section>
</template>

<script>
import HorizontalStepper from 'vue-stepper';
import axios from "axios";
// This components will have the content for each stepper step.
import StepOneLoad from './StepOneLoad.vue';
import StepTwoLoad from './StepTwoLoad.vue';
import StepThirdUnload from './StepThirdUnload.vue';
import StepFourLoad from './StepFourLoad.vue';


export default {
    components: {
        HorizontalStepper
    },
    data(){
        return {
            demoSteps: [
                {
                    icon: 'list',
                    name: 'first',
                    title: 'CARGUE/DESCARGUE CONTENEDOR',
                    subtitle: 'Información contenedor',
                    component: StepOneLoad,
                    completed: false

                },
                {
                    icon: 'assignment',
                    name: 'second',
                    title: 'INFORMACIÓN GENERAL',
                    subtitle: 'Información cliente',
                    component: StepTwoLoad,
                    completed: false

                },
                {
                    icon: 'dashboard',
                    name: 'third',
                    title: 'HOJA BINGO',
                    subtitle: 'Validación items',
                    component: StepThirdUnload,
                    completed: false

                },
                {
                    icon: 'description',
                    name: 'third',
                    title: 'CONSOLIDADO CONTENEDOR',
                    subtitle: 'Información final ',
                    component: StepFourLoad,
                    completed: false

                }
            ],
            hour_end : ""
        }
    },
    methods: {
        
        getNow() {
                    const today = new Date();                    
                    const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                    this.hour_end = time;
        },
        // Executed when @completed-step event is triggered
        completeStep(payload) {
            this.demoSteps.forEach((step) => {
                if (step.name === payload.name) {
                    step.completed = true;
                }
            })
        },
        // Executed when @active-step event is triggered
        isStepActive(payload) {
            this.demoSteps.forEach((step) => {
                if (step.name === payload.name) {
                    if(step.completed === true) {
                        step.completed = false;
                    }
                }
            })
        },
        // Executed when @stepper-finished event is triggered
        alert() {   
            this.getNow();                     
            this.load_unload_table_json = JSON.parse(localStorage.getItem("load_unload_table") || '[]');
            let load_unload_table = {
                "inventory_load_unload_id": 0,
                "container_type": this.load_unload_table_json["container"],
                "container_number": parseInt(this.load_unload_table_json['containerNumber']),
                "tare": this.load_unload_table_json["tare"],
                "hour_start": this.load_unload_table_json["hourStart"],
                "hour_end": this.hour_end,
                "space": this.load_unload_table_json["space"],
                "number_photos": parseInt(this.load_unload_table_json['photosNumber']),
                "client_name": this.load_unload_table_json["clientName"],
                "inventory_reference": this.load_unload_table_json["reference"],
                "inventory_date": this.load_unload_table_json["date"],
                "total_pieces": parseInt(this.load_unload_table_json['totalPieces']),
                "total_vans": parseInt(this.load_unload_table_json['totalVans']),
                "volume_m3": this.load_unload_table_json["volumeM3"],
                "received_by": this.load_unload_table_json["received"],
                "delivered_by": this.load_unload_table_json["delivered"],
                "personnel": this.load_unload_table_json["personnel"],
                "packing": this.load_unload_table_json["packing"],
                "personnel1": this.load_unload_table_json["personnel1"],
                "load_unload": this.load_unload_table_json["load"],
                "seals": parseInt(this.load_unload_table_json['seals']),
                "license_plate": this.load_unload_table_json["licensePlate"],
                "consolidated": this.load_unload_table_json["consolidated"],
                "observations": this.load_unload_table_json["observations"]
            }
            axios.post("http://127.0.0.1:8000/load_unload", load_unload_table).then((result) => {
                console.log(result);
            });


            this.inventory_load_unload_json = JSON.parse(localStorage.getItem("inventory_load_unload") || '[]');
            for (const index in this.inventory_load_unload_json) {
                
                let inventory_load_unload = this.inventory_load_unload_json[index]
                axios.put("http://127.0.0.1:8000/update_items/" + inventory_load_unload['barcode_id'], inventory_load_unload).then((result) => {
                console.log(result);
            });
            }
            axios.put("http://127.0.0.1:8000/update_inventory/" + load_unload_table["inventory_reference"] + "?status=unload").then((result) => {
                console.log(result);
            });

            let load_unload_email = {
                "email": [
                    "fobiber773@yeafam.com"
                    ],
                "body": {
                    "info_general_load_unload" : load_unload_table,
                        "info_items": this.inventory_load_unload_json},
                "subject": "TEST WITH UNLOAD PROCESS"
            };

            axios.post("http://127.0.0.1:8000/email", load_unload_email).then((result) => {
                console.log(result);
            });

            this.$router.push('/home');            

        }
    }
}
</script>

<style scoped>

.container{
    
  margin-top: 5%;
}

.content {
    margin-top: 5%;
}

</style>