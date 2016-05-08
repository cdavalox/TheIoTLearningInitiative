for mod in `cat /proc/modules | cut -d " " -f 1`
    do
        desc=`modinfo -d $mod`
        printf "%-20s $desc\n" "$mod:"
    done
