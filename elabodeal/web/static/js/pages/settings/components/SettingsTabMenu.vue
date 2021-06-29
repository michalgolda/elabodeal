<template>
	<div class="section">
        <p class="section__title">Ustawienia</p>
        <div class="link-list">
            <template v-for="tab in tabs">
                <div 
                    class="link flex-center"
                    :class="{ 'link__current': currentTabName === tab.name }"
                >
                    <a 
                        href=""
                        @click.prevent="() => showTab(tab.name)"
                    >
                        <p>{{ tab.linkText }}</p>
                    </a>
                </div>
            </template>
        </div>
    </div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapState, mapMutations, mapGetters } = createNamespacedHelpers('ui');


export default {
    computed: mapGetters(['currentTabName']),
    data() {
        return {
            tabs: [
                {
                    name: 'user',
                    linkText: 'Użytkownik'
                },
                {
                    name: 'publisher',
                    linkText: 'Sprzedający'
                }
            ]
        }
    },
    methods: mapMutations(['showTab'])
}
</script>