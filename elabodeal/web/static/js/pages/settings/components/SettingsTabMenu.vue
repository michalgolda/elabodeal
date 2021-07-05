<template>
	<div class="section">
        <p class="section__title">
            Ustawienia
        </p>
        <div class="link-list">
            <div 
                class="link flex-center"
                :class="{ 'link__current': currentTabName === tab.name }"
                v-for="tab in tabs"
                :key="tab.name"
            >
                <a 
                href=""
                    @click.prevent="() => showTab(tab.name)"
                >
                    <p>{{ tab.linkText }}</p>
                </a>
            </div>
        </div>
    </div>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

const { mapMutations, mapGetters } = createNamespacedHelpers('ui');


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