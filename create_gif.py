import imageio
import os

def create_gif(data_dir, gif_name, list_files):
    with imageio.get_writer(os.path.join(data_dir,gif_name), mode='I') as writer:
        for file_ in list_files:
            image = imageio.imread(os.path.join(data_dir,file_))
            writer.append_data(image)

any_direction = ['image_init.png','image_0.1.png', 'image_0.2.png', 'image_0.3.png', 'image_0.4.png', 'image_0.5.png', 'image_0.6.png', 'image_0.7.png', 'image_0.8.png', 'image_0.9.png', 'image_1.0.png']

diff_direction = ['image_init.png','image_diff_0.1.png', 'image_diff_0.2.png', 'image_diff_0.3.png', 'image_diff_0.4.png', 'image_diff_0.5.png', 'image_diff_0.6.png', 'image_diff_0.7.png', 'image_diff_0.8.png', 'image_diff_0.9.png', 'image_diff_1.0.png','image_final.png']

two_files = ['image_init.png', 'image_final.png']

folder = '/workspace/data/Experiments/nerf/dnerf_latent/project_results/latent_init_bballs_001'
create_gif(folder, 'unit_dir.gif', any_direction)
create_gif(folder, 'diff_dir.gif', diff_direction)
create_gif(folder, 'start_to_end.gif', two_files)