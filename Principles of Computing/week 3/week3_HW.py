TEST_CASES = [0, 5999, 700, 1900, 1270, 10, 700, 5999, 1900, 1909]

#def format(run_time):
#    global run_time_str, d_run_time
#    bc_run_time = (run_time / 10)
#    d_run_time = (run_time % 10)
#    if (bc_run_time > 59):
#        a_run_time = (bc_run_time / 60)
#        bc_run_time = (bc_run_time - (60 * a_run_time))
#    else:
#        a_run_time = 0
#    if (bc_run_time > 10):
#        str_current_time = ((((str(a_run_time) + ':') + str(bc_run_time)) + '.') + str(d_run_time))
#    else:
#        str_current_time = (((((str(a_run_time) + ':') + '0') + str(bc_run_time)) + '.') + str(d_run_time))
#    return str_current_time
#

##print format(5999)

#def format(t):
#    if (t <= 9):
#        A = '0'
#        B = '0'
#        C = '0'
#    elif (len(str(t)) == 2):
#        A = '0'
#        B = '0'
#        C = (t // 10)
#    else:
#        A = (t // 600)
#        t = (t % 600)
#        if (len(str(t)) == 3):
#            B = ((t // 10) // 10)
#            C = ((t // 10) % 10)
#        elif (len(str(t)) < 3):
#            if (t <= 59):
#                B = '0'
#                C = (t // 10)
#            else:
#                B = (((t % 60) // 10) % 10)
#                C = (t // 10)
#    D = (t % 10)
#    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))

#def format(t):
#    a = (t // 600)
#    b = (((t % 600) / 10) / 10)
#    c = '0'
#    if (t > 10):
#        c = str(t)[(-2)]
#    d = str(t)[(-1)]
#    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
#    return formatedTime
#
#for i in range(0, 5999):
#    print i, " : ", format(i)