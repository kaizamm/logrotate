/opt/logrotate.py:
  file.managed:
    - source: salt://logrotate_files/files/logrotate.py
    - user: root
    - group: root
    - mode: 755
  cmd.run:
    - name: python /opt/logrotate.py {{ pillar['log_path'] }} {{ pillar['bak_path_'] }} {{ pillar['save_days'] }}
    - require: 
      - file: /opt/logrotate.py

