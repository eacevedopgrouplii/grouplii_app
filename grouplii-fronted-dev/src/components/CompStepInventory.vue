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
import StepOneInventory from './StepOneInventory.vue';
import StepTwoInventory from './StepTwoInventory.vue';
import StepThirdInventory from './StepThirdInventory.vue';

export default {
    components: {
        HorizontalStepper
    },
    data(){
        return {
            demoSteps: [
                {
                    icon: 'assignment',
                    name: 'first',
                    title: 'General',
                    subtitle: 'Completar información',
                    component: StepOneInventory,
                    completed: false
                },
                {
                    icon: 'assignment_turned_in',
                    name: 'second',
                    title: 'Envío',
                    subtitle: 'Completar información',
                    component: StepTwoInventory,
                    completed: false
                },
                {
                    icon: 'add_to_photos',
                    name: 'third',
                    title: 'Descripción',
                    subtitle: 'Completar información',
                    component: StepThirdInventory,
                    completed: true
                }
            ],            
            inventory_table : [],
            inventory_table_detail : [],
        }
    },
    methods: {
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
        alert(payload) {
            
            
            console.log(payload);
            this.inventory_table = JSON.parse(localStorage.getItem("inventory_table") || '[]');
            this.inventory_table_detail = JSON.parse(localStorage.getItem("inventory_table_detail") || '[]');
            let inventory_table_complete = {
                "inventory_id": 0,
                "inventory_process": this.inventory_table['process'],
                "clients_name": this.inventory_table['clientname'],
                "inventory_reference": this.inventory_table['reference'],
                "inventory_origin": this.inventory_table['origin'],
                "inventory_phone": this.inventory_table['phone'],
                "inventory_email": this.inventory_table['email'],
                "inventory_destination": this.inventory_table['destination'],
                "inventory_via": this.inventory_table['via'],
                "status_inventory" : "packing"
            };

            let config_email = this.inventory_table['email_send'].split(',');
            config_email.push(this.inventory_table['email'])


            let post_email = {
                "email": config_email,
                "body": {"info_general_inventory" :this.inventory_table, "info_detail" : this.inventory_table_detail},
                "subject": "INVENTORY PROCESS " + this.inventory_table['clientname'] + " / " + this.inventory_table['reference']
                }

            axios.post("https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/create_inventory", inventory_table_complete).then((result) => {
                console.log(result);
            });

            
            for (const index in this.inventory_table_detail) {
                let detail = this.inventory_table_detail[index]
                console.log(this.inventory_table_detail);
                let inventory_detail_table_complete = {
                    "item_id": 0,
                    "inventory_id": this.inventory_table['reference'],
                    "barcode_id": parseInt(detail['barcode']),
                    "item_number": parseInt(detail['item']),
                    "packing_reference": detail['packing'],
                    "articles": detail['articles'],
                    "condition_at_origin": detail['condition'],
                    "exceptions_at_destination": detail['exceptions'],
                    "load_check": false,
                    "description_unload": " ",
                    "unload_check": false,
                    "description_load" : " "

                }
                console.log(inventory_detail_table_complete);
                axios.post("https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/create_inventory_detail", inventory_detail_table_complete).then((result) => {
                console.log(result);
                });
            }

            axios.post("https://container-grouplii-backend-uymd3d36pa-uc.a.run.app/email", post_email).then((result) => {
                console.log(result);
            });

            console.log("Text Ok");

            this.$router.psuh('home/operator');
            
        }   
    }
}
</script>

<style scoped>

.container {
    margin-top: 5%;
}

</style>



