First Run phase_1 map and reduce files then the output is fed to Phase_2 map and reduce

hadoop jar /usr/hdp/2.3.0.0-2557/hadoop-mapreduce/hadoop-streaming-2.7.1.2.3.0.0-2557.jar -D mapred.map.tasks=2 -D mapred.reduce.tasks=1 -files "<phase_1 map_location>","<phase_1 reduce_location>" -mapper "<Map_1 filename>" -reducer "<reduce_1 file name>" -input <input file> -output <output file>

hadoop fs -get /market/output/part-00000


hadoop jar /usr/hdp/2.3.0.0-2557/hadoop-mapreduce/hadoop-streaming-2.7.1.2.3.0.0-2557.jar -D mapred.map.tasks=2 -D mapred.reduce.tasks=1 -files "<pahse_2 map>","<phase_2 reduce>",-cacheFile <output of fist phase>#<tag_name> -mapper "<phase_2 map file>" -reducer "<phase_2 reduce file>" -input <input file> -output <output_file>

hadoop fs -get /market/output2/part-00000