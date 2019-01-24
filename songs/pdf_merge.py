from PyPDF2 import PdfFileMerger

pdfs =  ['aguas_de_marco.pdf', 'ainda_e_cedo.pdf', 'all_star.pdf', 'another_brick_in_the_wall.pdf', 'azul_da_cor_do_mar.pdf', 'back_in_black.pdf', 'blackbird.pdf', 'blue_suede_shoes.pdf', 'burguesinha.pdf', 'chao_de_giz.pdf', 'comfortably_numb.pdf', 'down_by_the_river.pdf', 'easy.pdf', 'faroeste_caboclo.pdf', 'fix_you.pdf', 'garota_de_ipanema.pdf', 'ha_tempos.pdf', 'hallelujah.pdf', 'happiness_is_a_warm_gun.pdf', 'help!.pdf', 'here_there_and_everywhere.pdf', 'hey_jude.pdf', 'hotel_california.pdf', 'imagine.pdf', 'lady_madonna.pdf', 'love_yourself.pdf', 'monte_castelo.pdf', "mother_nature's-son.pdf", "mother_nature's_son.pdf", 'nem_um_dia.pdf', 'no_woman_no_cry.pdf', 'nothing_else_matters.pdf', 'one.pdf', 'os_cegos_do_castelo.pdf', 'pais_e_filhos.pdf', 'primavera.pdf', 'redemption_song.pdf', 'sina.pdf', 'something.pdf', 'sultans_of_swing.pdf', 'tears_in_heaven.pdf', 'tempo_perdido.pdf', 'thinking_out_loud.pdf', 'three_little_birds.pdf', 'twist_and_shout.pdf', 'voce.pdf', 'wave.pdf', 'when_im_sixty_four.pdf', 'why_dont_we_do_it_in_the_road.pdf', 'wish_you_here.pdf', 'wonderful_tonight.pdf', "you've_got_a_friend_in_me.pdf", 'your_song.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))
    print(pdf)

with open('ola.pdf', 'wb') as fout:
    merger.write(fout)