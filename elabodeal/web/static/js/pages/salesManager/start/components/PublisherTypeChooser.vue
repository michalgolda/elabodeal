<template>
    <div class="chooser flex-center">
        <div class="wrapper">
            <h1 class="chooser__title">
                Wybierz typ konta
            </h1>
            <p class="chooser__description">
                awdakwdkajwkdjawkdjawkdjawkdjakwd
            </p>
            <div class="chooser__optionList flex-center">
                <div 
                    @click="handleChoose"
                    class="chooser__option flex-center"
                >
                    <div>
                        <i class="fas fa-user-alt" />
                        <p>Wydawca indywidualny</p>
                    </div>
                </div>
                <div 
                    @click="handleChoose"
                    class="chooser__option flex-center"
                >
                    <div>
                        <i class="fas fa-building" />
                        <p>Wydawnictwo</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapMutations: mapUiMutations } = createNamespacedHelpers('ui');


export default {
    methods: {
        ...mapUiMutations(['setFormType']),
        handleChoose () {
            this.setFormType('invidual');
        }
    }
}
</script>