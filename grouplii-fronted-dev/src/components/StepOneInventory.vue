<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <div class="col-sm-3">             
            <label class="label">Seleccione proceso: </label>
            <select :class="['input', ($v.form.process.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.process">>
                <option value="NacionalSin">Nacional Sin Almacenaje</option>
                <option value="NacionalCon">Nacional Con Almacenaje</option>
                <option value="Internacional">Internacional</option>
            </select>
        </div>
        
        <div class="field">
            <label class="label">CLIENTS NAME:</label>
            <div class="control">
                <input :class="['input', ($v.form.clientname.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.clientname">
            </div>
        </div>
        <div class="field">
            <label class="label">REF:</label>
            <div class="control">
                <input :class="['input', ($v.form.reference.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.reference">
            </div>
        </div>
        <div class="field">
            <label class="label">ORIGIN:</label>
            <div class="control">
                <input :class="['input', ($v.form.origin.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.origin">
            </div>
        </div>
        <div class="field">
            <label class="label">PHONE no:</label>
            <div class="control">
                <input :class="['input', ($v.form.phone.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.phone">
            </div>
        </div>
        <div class="field">
            <label class="label">EMAIL:</label>
            <div class="control">
                <input :class="['input', ($v.form.email.$error) ? 'is-danger' : '']"  type="text" placeholder="Email input" v-model="form.email">
            </div>
            <p v-if="$v.form.email.$error" class="help is-danger">This email is invalid</p>
        </div>        
    </div>
</template>

<script>import {validationMixin} from 'vuelidate'
    import {required} from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                form: {                    
                    process: '',
                    clientname: '',
                    reference: '',
                    origin: '',
                    phone: '',
                    email: '',
                }
            }
        },
        validations: {
            form: {
                process: {
                    required
                },
                clientname: {
                    required
                },
                reference: {
                    required
                },
                origin: {
                    required
                },
                phone: {
                    required
                },
                email: {
                    required,                   
                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if(!val.$invalid) {
                        this.$emit('can-continue', {value: true});
                        localStorage.setItem('inventory_table',JSON.stringify(this.form));
                    } else {
                        this.$emit('can-continue', {value: false});
                    }
                },
                deep: true
            },
            clickedNext(val) {
                if(val === true) {
                    this.$v.form.$touch();                    
                }
            },
            
        },
        mounted() {
            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});                
            } else {
                this.$emit('can-continue', {value: false});
            }
        }
    }
</script>