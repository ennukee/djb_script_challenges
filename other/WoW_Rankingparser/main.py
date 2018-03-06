def main():
    boss_i = -1
    out = {}
    with open('fights/fights.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            spl = line.split()
            if len(spl) == 1:
                # new boss
                boss_i += 1
            else:
                name = spl[4]
                if name not in out.keys():
                    out[name] = ['-1' for i in range(10)]
                out[name][boss_i] = spl[0]
    print(out)
    conv_out = ["{},{}".format(k, ",".join(out[k])) for k in out.keys()]
    with open('fights/out.txt', 'w') as f:
        f.write('\n'.join(conv_out))

if __name__ == "__main__":
    main()
