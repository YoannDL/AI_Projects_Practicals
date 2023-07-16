import tkinter as tk

# Destinations and their attributes
destinations = {
    'united_states': ['diverse_landscapes', 'metropolitan_cities', 'cultural_diversity', 'national_parks'],
    'spain': ['vibrant_culture', 'beaches', 'architecture', 'tapas', 'fiestas'],
    'france': ['art_and_culture', 'historical_landmarks', 'gastronomy', 'wine', 'fashion'],
    'italy': ['ancient_ruins', 'artistic_heritage', 'culinary_delights', 'coastlines', 'fashion'],
    'china': ['rich_heritage', 'ancient_landmarks', 'cuisine', 'diverse_landscapes', 'modern_cities'],
    'mexico': ['ancient_civilizations', 'beaches', 'culinary_delights', 'festivals', 'colorful_traditions'],
    'united_kingdom': ['historical_sites', 'royal_heritage', 'theater', 'pub_culture', 'countryside'],
    'turkey': ['historical_sites', 'breathtaking_landscapes', 'hospitality', 'cuisine', 'bazaars'],
    'germany': ['rich_history', 'castles', 'beer', 'festivals', 'technological_innovation'],
    'thailand': ['buddhist_temples', 'exotic_cuisine', 'tropical_beaches', 'elephant_sanctuaries', 'night_markets'],
    'malaysia': ['diverse_cultures', 'beaches', 'rainforests', 'street_food', 'modern_architecture'],
    'canada': ['breathtaking_landscapes', 'wildlife', 'multicultural_cities', 'outdoor_activities', 'parks'],
    'russia': ['world-class_museums', 'historical_landmarks', 'vast_landscapes', 'ballet', 'winter_sports'],
    'japan': ['ancient_traditions', 'technology', 'temples', 'onsen', 'sushi'],
    'australia': ['stunning_beaches', 'outback_landscapes', 'diverse_wildlife', 'surfing', 'vibrant_cities'],
    'greece': ['ancient_ruins', 'island_hopping', 'mediterranean_cuisine', 'beaches', 'history'],
    'brazil': ['vibrant_culture', 'carnival', 'beaches', 'rainforests', 'samba_music'],
    'india': ['rich_history', 'spirituality', 'diverse_cuisine', 'monuments', 'colorful_festivals'],
    'south_africa': ['wildlife_safaris', 'adventure_sports', 'wine_regions', 'diverse_cultures', 'breathtaking_landscapes'],
    'argentina': ['tango_music_and_dance', 'steakhouses', 'glaciers', 'wine_regions', 'patagonia'],
    'egypt': ['ancient_civilizations', 'pyramids', 'nile_river', 'sphinx', 'historical_sites'],
    'indonesia': ['tropical_paradise', 'temples', 'beaches', 'volcanoes', 'traditional_arts'],
    'netherlands': ['canals', 'windmills', 'cycling_culture', 'art_museums', 'tulip_fields'],
    'peru': ['incan_ruins', 'amazon_rainforest', 'machu_picchu', 'traditional_culture', 'culinary_delights'],
    'vietnam': ['breathtaking_landscapes', 'ancient_temples', 'street_food', 'rice_terraces', 'cultural_heritage'],
    'portugal': ['historic_cities', 'coastal_beauty', 'vineyards', 'pastries', 'fado_music'],
    'colombia': ['colorful_cities', 'coffee_plantations', 'caribbean_beaches', 'salsa_music', 'emerald_mines'],
    'new_zealand': ['adventure_sports', 'spectacular_landscapes', 'maori_culture', 'wineries', 'hiking_trails'],
    'sweden': ['scenic_landscapes', 'medieval_architecture', 'design', 'fika_culture', 'northern_lights'],
    'austria': ['imperial_history', 'alpine_landscapes', 'music', 'coffeehouses', 'christmas_markets'],
    'switzerland': ['alpine_beauty', 'skiing', 'chocolate', 'watchmaking', 'efficiency'],
    'belgium': ['chocolate', 'beer', 'medieval_towns', 'architecture', 'comic_strips'],
    'morocco': ['vibrant_markets', 'desert_landscapes', 'mosques', 'traditional_crafts', 'tagine'],
    'denmark': ['cozy_hygge_concept', 'bicycle-friendly_cities', 'fairy-tale_castles', 'nordic_cuisine', 'design'],
    'ireland': ['lush_landscapes', 'castles', 'pub_culture', 'traditional_music', 'friendly_locals'],
    'norway': ['fjords', 'northern_lights', 'viking_history', 'outdoor_adventures', 'scenic_train_rides'],
    'czech_republic': ['medieval_architecture', 'beer_culture', 'music_festivals', 'cultural_heritage', 'bohemian_crystal'],
    'israel': ['religious_sites', 'historical_landmarks', 'beaches', 'culinary_delights', 'innovation'],
    'hungary': ['thermal_baths', 'historic_sites', 'ruin_pubs', 'goulash', 'folklore'],
    'finland': ['midnight_sun', 'saunas', 'arctic_beauty', 'design', 'winter_sports'],
    'croatia': ['adriatic_coastline', 'historical_cities', 'island_hopping', 'seafood', 'game_of_thrones_filming_locations'],
    'singapore': ['modern_architecture', 'shopping', 'cultural_diversity', 'street_food', 'gardens'],
    'poland': ['historical_landmarks', 'medieval_cities', 'pierogi', 'vibrant_festivals', 'natural_beauty'],
    'philippines': ['tropical_islands', 'beaches', 'diving_spots', 'rice_terraces', 'friendly_locals'],
    'chile': ['diverse_landscapes', 'patagonia', 'atacama_desert', 'wine_regions', 'easter_island'],
    'iceland': ['glaciers', 'volcanoes', 'waterfalls', 'geothermal_hot_springs', 'northern_lights'],
    'saudi_arabia': ['ancient_history', 'islamic_culture', 'desert_landscapes', 'mosques', 'traditional_arts'],
    'united_arab_emirates': ['luxury', 'modern_architecture', 'desert_safaris', 'shopping', 'beaches'],
    'south_korea': ['k-pop_culture', 'historical_palaces', 'technology', 'spicy_cuisine', 'shopping'],
    'romania': ['medieval_castles', 'transylvania', 'carpathian_mountains', 'folklore', 'traditional_villages'],
    'ukraine': ['historical_landmarks', 'orthodox_churches', 'carpathian_mountains', 'cultural_heritage', 'borscht'],
    'jamaica': ['reggae_music', 'beaches', 'waterfalls', 'rum', 'laid-back_vibes'],
    'bulgaria': ['historic_cities', 'black_sea_coast', 'ski_resorts', 'rose_oil', 'traditional_music_and_dance'],
    'cyprus': ['mediterranean_charm', 'beaches', 'ancient_ruins', 'hospitality', 'cypriot_cuisine'],
    'costa_rica': ['biodiversity', 'rainforests', 'beaches', 'adventure_activities', 'ecotourism'],
    'tunisia': ['mediterranean_beaches', 'ancient_ruins', 'souks', 'traditional_music', 'desert_landscapes'],
    'estonia': ['medieval_towns', 'baltic_sea_coast', 'technology', 'saunas', 'song_and_dance_festivals'],
    'slovenia': ['lake_bled', 'mountain_landscapes', 'caves', 'wine_regions', 'ljubljana'],
    'lithuania': ['baltic_coast', 'medieval_architecture', 'amber', 'folklore', 'curonian_spit'],
    'latvia': ['riga', 'baltic_sea_coast', 'art_nouveau_architecture', 'festivals', 'traditional_cuisine'],
    'malta': ['historic_sites', 'mediterranean_charm', 'beaches', 'cultural_festivals', 'azure_window'],
    'slovakia': ['castles', 'carpathian_mountains', 'caves', 'folk_traditions', 'spa_towns'],
    'luxembourg': ['medieval_castles', 'picturesque_towns', 'european_union_institutions', 'moselle_wine', 'multilingualism'],
    'qatar': ['modern_architecture', 'desert_landscapes', 'cultural_heritage', 'luxury', 'traditional_souqs'],
    'bahrain': ['modern_architecture', 'pearl_diving', 'cultural_heritage', 'formula_1_racing', 'spice_markets'],
    'oman': ['desert_landscapes', 'ancient_forts', 'wadis', 'traditional_culture', 'frankincense'],
    'panama': ['panama_canal', 'tropical_rainforests', 'beaches', 'indigenous_culture', 'cosmopolitan_capital'],
    'uruguay': ['beaches', 'gauchos', 'tango_music_and_dance', 'wine_regions', 'colonial_architecture'],
    'kuwait': ['modern_architecture', 'desert_landscapes', 'shopping', 'islamic_culture', 'souqs'],
    'andorra': ['ski_resorts', 'mountain_landscapes', 'duty-free_shopping', 'hiking_trails', 'romanesque_architecture'],
    'belarus': ['soviet-era_architecture', 'museums', 'national_parks', 'traditional_cuisine', 'hospitality'],
    'serbia': ['rich_history', 'orthodox_monasteries', 'music_festivals', 'rakija', 'traditional_folklore'],
    'georgia': ['ancient_churches', 'mountain_landscapes', 'wine_regions', 'traditional_cuisine', 'hospitality'],
    'armenia': ['ancient_monasteries', 'mountain_landscapes', 'cultural_heritage', 'apricots', 'hospitality'],
    'lebanon': ['historical_sites', 'mediterranean_cuisine', 'nightlife', 'beaches', 'roman_ruins'],
    'moldova': ['wine_regions', 'cultural_heritage', 'monasteries', 'traditional_crafts', 'hospitality'],
    'albania': ['mediterranean_beaches', 'historical_sites', 'mountain_landscapes', 'traditional_culture', 'hospitality'],
    'montenegro': ['adriatic_coastline', 'bay_of_kotor', 'mountain_landscapes', 'historical_towns', 'outdoor_activities'],
    'north_macedonia': ['historical_sites', 'lakes', 'mountain_landscapes', 'traditional_cuisine', 'hospitality'],
    'bosnia_herzegovina': ['historic_cities', 'natural_beauty', 'cultural_heritage', 'balkan_cuisine', 'hospitality'],
    'kazakhstan': ['vast_landscapes', 'mountains', 'steppe', 'nomadic_culture', 'modern_architecture', 'hospitality'],
    'azerbaijan': ['historic_landmarks', 'fire_temples', 'caspian_sea_coast', 'mud_volcanoes', 'hospitality'],
    'ecuador': ['diverse_landscapes', 'galapagos_islands', 'amazon_rainforest', 'indigenous_culture', 'adventure_activities'],
    'paraguay': ['iguazu_falls', 'riverside_towns', 'mate_tea', 'guarani_culture', 'chaco_region'],
    'nepal': ['himalayas', 'mountain_trekking', 'buddhist_temples', 'cultural_heritage', 'hospitality'],
    'dominican_republic': ['beaches', 'tropical_landscapes', 'merengue_music_and_dance', 'rum', 'adventure_sports'],
    'sri_lanka': ['ancient_ruins', 'tea_plantations', 'beaches', 'wildlife_safaris', 'spices'],
    'tanzania': ['wildlife_safaris', 'mount_kilimanjaro', 'zanzibar_beaches', 'maasai_culture', 'serengenti_national_park'],
    'kenya': ['wildlife_safaris', 'maasai_mara', 'beaches', 'mountain_landscapes', 'cultural_heritage'],
    'ghana': ['cultural_heritage', 'forts_and_castles', 'beaches', 'traditional_music_and_dance', 'hospitality'],
    'cameroon': ['diverse_landscapes', 'mountain_trekking', 'wildlife', 'traditional_culture', 'hospitality'],
    'botswana': ['wildlife_safaris', 'okavango_delta', 'chobe_national_park', 'traditional_culture', 'hospitality'],
    'uganda': ['mountain_gorillas', 'wildlife_safaris', 'rwenzori_mountains', 'lake_victoria', 'cultural_heritage'],
    'zambia': ['victoria_falls', 'wildlife_safaris', 'river_cruises', 'adventure_activities', 'cultural_heritage'],
    'maldives': ['tropical_paradise', 'beaches', 'snorkeling', 'luxury_resorts', 'underwater_dining'],
    'zimbabwe': ['victoria_falls', 'wildlife_safaris', 'great_zimbabwe_ruins', 'adventure_activities', 'hospitality'],
    'ethiopia': ['ancient_civilizations', 'rock-hewn_churches', 'simien_mountains', 'coffee_culture', 'cultural_heritage'],
    'madagascar': ['unique_wildlife', 'rainforests', 'beaches', 'baobab_trees', 'traditional_culture'],
    'rwanda': ['mountain_gorillas', 'volcanoes', 'lake_kivu', 'cultural_heritage', 'hospitality'],
    'namibia': ['desert_landscapes', 'wildlife_safaris', 'skeleton_coast', 'tribal_culture', 'scenic_beauty']
}

def suggest_destination():
    preferences = preferences_entry.get().split(',')
    matching_destinations = []

    for destination, attributes in destinations.items():
        if all(pref in attributes for pref in preferences):
            matching_destinations.append(destination)

    if matching_destinations:
        suggested_destinations_text.configure(state='normal')
        suggested_destinations_text.delete('1.0', tk.END)
        suggested_destinations_text.insert(tk.END, '\n'.join(matching_destinations))
        suggested_destinations_text.configure(state='disabled')
    else:
        suggested_destinations_text.configure(state='normal')
        suggested_destinations_text.delete('1.0', tk.END)
        suggested_destinations_text.insert(tk.END, 'No destination suggestions based on your preferences.')
        suggested_destinations_text.configure(state='disabled')

# Create the main window
window = tk.Tk()
window.title('Destination Suggestion')
window.geometry('400x300')

# Create the preferences label and entry
preferences_label = tk.Label(window, text='Enter your preferences (separated by commas):')
preferences_label.pack()

preferences_entry = tk.Entry(window)
preferences_entry.pack()

# Create the suggestion button
suggestion_button = tk.Button(window, text='Get Suggestions', command=suggest_destination)
suggestion_button.pack()

# Create the suggested destinations text box
suggested_destinations_text = tk.Text(window, height=10, width=30, state='disabled')
suggested_destinations_text.pack()

# Start the GUI event loop
window.mainloop()
