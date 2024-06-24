from country_viz import make_dataset, process_data # Functions
#from country_viz import c # Dict with the config

if __name__ == '__main__':

    make_dataset.download_data()
    make_dataset.clean_data()
    process_data.process_data()