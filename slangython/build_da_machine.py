import sys
sys.path.append('..')
from transducer.module import *

def build_da_machine():
	machine = FiniteStateTranducer()

	statement_point = machine.add_point(isFinal_=True, parrot_=True)
	expression_point = machine.add_point(isFinal_=True, parrot_=True)
	comment_point = machine.add_point(isFinal_=True, parrot_=True)

	#print('statement_point: ', statement_point)
	#print('expression_point: ', expression_point)
	#print('comment_point: ', comment_point)

	# all the math notations
	machine.points[expression_point].add_quick_transition(['SUM'],expression_point,'+')
	machine.points[expression_point].add_quick_transition(['DIFF'],expression_point,'-')
	machine.points[expression_point].add_quick_transition(['PRODUKT'],expression_point,'*')
	machine.points[expression_point].add_quick_transition(['QUOSHUNT'],expression_point,'/')
	machine.points[expression_point].add_quick_transition(['MOD'],expression_point,'%')

	# boolean
	machine.points[expression_point].add_quick_transition([':)'],expression_point,'True')
	machine.points[expression_point].add_quick_transition([':('],expression_point,'False')
	machine.points[expression_point].add_quick_transition(['AND'],expression_point,'and')
	machine.points[expression_point].add_quick_transition(['OR'],expression_point,'or')

	saem_point = machine.add_point() # isFinal_ defaults to False
	machine.points[expression_point].add_quick_transition(['SAEM'],saem_point,'')
	machine.points[saem_point].add_quick_transition(['AS'],expression_point,'==')

	biggr_point = machine.add_point() 
	machine.points[expression_point].add_quick_transition(['BIGGR'],biggr_point,'')
	machine.points[biggr_point].add_quick_transition(['THAN'],expression_point,'>')

	smallr_point = machine.add_point() 
	machine.points[expression_point].add_quick_transition(['SMALLR'],smallr_point,'')
	machine.points[smallr_point].add_quick_transition(['THAN'],expression_point,'<')

	machine.points[expression_point].add_quick_transition(['LOL'],statement_point,':')
	machine.points[expression_point].add_quick_transition(['BTW'],comment_point,'#')
	machine.points[expression_point].add_quick_transition(['\n'],statement_point,'\n')

	# comment
	machine.points[comment_point].add_quick_transition(['\n'],statement_point,'\n') # default behavior is spitting out what is put in

	# statement
	machine.points[statement_point].add_quick_transition(['\n'],statement_point,'\n')
	machine.points[statement_point].add_quick_transition(['GTFO'],statement_point,'break')

	keep_point = machine.add_point()
	machine.points[statement_point].add_quick_transition(['KEEP'],keep_point,'')
	machine.points[keep_point].add_quick_transition(['GOIN'],statement_point,'continue')

	i_point = machine.add_point()
	machine.points[statement_point].add_quick_transition(['I'],i_point,'')
	i_has_point = machine.add_point()
	machine.points[i_point].add_quick_transition(['HAS'],i_has_point,'')
	machine.points[i_has_point].add_quick_transition(['A'],statement_point,'') # it could go to expression, doesn't matter

	machine.points[statement_point].add_quick_transition(['ITZ'],expression_point,'=')
	machine.points[statement_point].add_quick_transition(['JIC'],expression_point,'if')
	machine.points[statement_point].add_quick_transition(['JW'],expression_point,'elif')
	machine.points[statement_point].add_quick_transition(['JK'],expression_point,'else') # it could go to statement, doesn't matter

	im_point = machine.add_point()
	machine.points[statement_point].add_quick_transition(['IM'],im_point,'')
	im_in_point = machine.add_point()
	machine.points[im_point].add_quick_transition(['IN'],im_in_point,'')
	im_in_yr_point = machine.add_point()
	machine.points[im_in_point].add_quick_transition(['YR'],im_in_yr_point,'')
	im_in_yr_loop_point = machine.add_point()
	machine.points[im_in_yr_point].add_quick_transition(['LOOP'],im_in_yr_loop_point,'')
	machine.points[im_in_yr_loop_point].add_quick_transition(['LOL'],statement_point,'while True :')

	im_in_yr_loop_uppin_point = machine.add_point()
	machine.points[im_in_yr_loop_point].add_quick_transition(['UPPIN'],im_in_yr_loop_uppin_point,'')
	im_in_yr_loop_uppin_yr_point = machine.add_point(parrot_=True)
	machine.points[im_in_yr_loop_uppin_point].add_quick_transition(['YR'],im_in_yr_loop_uppin_yr_point,'for')
	im_in_yr_loop_uppin_yr_til_point = machine.add_point(parrot_=True)
	machine.points[im_in_yr_loop_uppin_yr_point].add_quick_transition(['TIL'],im_in_yr_loop_uppin_yr_til_point,'in range(')
	machine.points[im_in_yr_loop_uppin_yr_til_point].add_quick_transition(['LOL'],statement_point,'+ 1 ) :')

	show_point = machine.add_point()
	machine.points[statement_point].add_quick_transition(['SHOW'],show_point,'')
	show_yr_point = machine.add_point(parrot_=True)
	machine.points[show_point].add_quick_transition(['YR'],show_yr_point,'print(')
	machine.points[show_yr_point].add_quick_transition(['LMAO'],statement_point,')')


	machine.start_id = statement_point
	return machine



